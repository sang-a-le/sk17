import pandas as pd
import mysql.connector

class XLS2DB():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="ohgiraffers",
            password="ohgiraffers",
            database="cardb"
        )

        if self.connection.is_connected():
            print('@@@MySQL 서버에 성공적으로 연결@@@')

        self.cursor = self.connection.cursor()

        self.years = ['2020', '2021', '2022', '2023', '2024']
        self.areas = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
        self.ecos = ['전기', '수소']
        self.non_ecos = ['휘발유', '경유', '엘피지']
        self.car_types = ['승용']
        self.df = None
        self.engine_idex = 1
        self.eco_idex = 1
    
    def close(self):
        self.cursor.close()
        self.connection.close()
        print('@@@MySQL 연결 종료@@@')

    def table_reader(self, xls_path, header, sheet_name, is_nan=False): 
        
        df = pd.read_excel(xls_path, header=header, sheet_name=sheet_name)

        if is_nan:
            df['연료별'] = df['연료별'].fillna(method='ffill')  # 앞의 연료명을 채워 넣음

            mask = pd.notna(df[('시도별', '용도별')])
            df.loc[mask, ('시도별', '종별')] = df.loc[mask, ('시도별', '종별')].fillna(method='ffill')
        
        return df

    def make_db(self, year, xls_path, header, sheet_name, is_nan=False):

        self.df = self.table_reader(xls_path, header, sheet_name, is_nan)
        ## non_eco table

        for non_eco in self.non_ecos:
            for car_type in self.car_types:
                i = 3
                for area in self.areas:
                    mask = (
                        (self.df[('연료별', 'Unnamed: 0_level_1')] == f'{non_eco}') &
                        (self.df[('시도별', '종별')] ==  f'{car_type}') &
                        (self.df[('시도별', '용도별')] == '계')
                    )
                    result = int(self.df.loc[mask, (f'{area}', f'Unnamed: {i}_level_1')].iloc[0])

                    sql = """
                    SELECT car_code FROM car_info 
                    WHERE f_type = %s
                    """
                    values = (non_eco,)
                    self.cursor.execute(sql, values)
                    row = self.cursor.fetchone()

                    if row:
                        car_code = row[0]
                    else:
                        # 없으면 INSERT
                        sql = "INSERT INTO car_info (f_type) VALUES (%s)"
                        values = (non_eco,)
                        self.cursor.execute(sql, values)
                        car_code = self.cursor.lastrowid

                    sql = "INSERT INTO engine_car_info (idex, car_code," \
                    "year, area, total) VALUES" \
                    "(%s, %s, %s, %s, %s)"
                    values = (f'{self.engine_idex}', f'{car_code}', year, f'{area}', str(result))
                    self.cursor.execute(sql, values)
                    i += 1
                    self.engine_idex += 1

        ## eco table
        for eco in self.ecos:
            for car_type in self.car_types:
                i = 3
                for area in self.areas:
                    mask = (
                        (self.df[('연료별', 'Unnamed: 0_level_1')] == f'{eco}') &
                        (self.df[('시도별', '종별')] ==  f'{car_type}') &
                        (self.df[('시도별', '용도별')] == '계')
                    )
                    result = int(self.df.loc[mask, (f'{area}', f'Unnamed: {i}_level_1')].iloc[0])

                    sql = """
                    SELECT car_code FROM car_info 
                    WHERE f_type = %s
                    """
                    values = (eco,)
                    self.cursor.execute(sql, values)
                    row = self.cursor.fetchone()

                    if row:
                        car_code = row[0]
                    else:
                        # 없으면 INSERT
                        sql = "INSERT INTO car_info (f_type) VALUES (%s)"
                        values = (eco,)
                        self.cursor.execute(sql, values)
                        car_code = self.cursor.lastrowid

                    sql = "INSERT INTO eco_car_info (idex, car_code," \
                    "year, area, total) VALUES" \
                    "(%s, %s, %s, %s, %s)"
                    values = (f'{self.eco_idex}', f'{car_code}', year, f'{area}', str(result))
                    self.cursor.execute(sql, values)
                    i += 1
                    self.eco_idex += 1

        self.connection.commit()

    def make_subsidy(self, ev, hd):

            sql = """
            SELECT idex, car_code, year, area 
            FROM eco_car_info
            """
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            
            for row in rows:
                print(f"row: {row}")
                idex = row[0]
                car_code = row[1]
                year = row[2]
                area = row[3]
                if car_code == 4:
                    target_dict = ev[int(str(year)[-1])]
                elif car_code == 5:
                    target_dict = hd[int(str(year)[-1])]
                else:
                    print(f"⚠️ 예상치 못한 car_code: {car_code}, row: {row}")
                    continue  # 또는 raise

                sql = "INSERT INTO subsidy (idex, car_code," \
                "year, area, amount) VALUES" \
                "(%s, %s, %s, %s, %s)"
                values = (idex, car_code, year, area, target_dict[area])
                self.cursor.execute(sql, values)