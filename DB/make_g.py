#import pymysql
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

connection = mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database = 'cardb'
    )

# # if connection.is_connected() : 
# #     print('@@@mysql 서버에 정상적으로 연결@@')

# # cursor = connection.cursor()


sql = 'select * from eco_car_info' 

df = pd.read_sql(sql, con=connection)

# print(df.head)

# cursor.execute(sql)   

# result_rows = cursor.fetchall()

# for row in result_rows :       
#     print(row)

# cursor.close()       
connection.close()

# print(df.head)

##------------------------------

# x = [1, 2, 3, 4, 5]
# y1 = [10, 20, 25, 30, 40]
# y2 = [15, 25, 35, 45, 55]

# # 두 개의 선 추가
# plt.plot(x, y1, label="Dataset 1", linestyle='--', color='b')
# plt.plot(x, y2, label="Dataset 2", linestyle='-', color='g')
# plt.legend()  # 범례 추가
# plt.title("Multiple Line Graphs")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# print(df.[year])
# df2 = df[df['year']==2020] and df[df['car_code']==4]
# print(df2)
# df3 = df[df['year']==2021]
# df4 = df[df['year']==2022]
# df5 = df[df['year']==2023]
# df6 = df[df['year']==2024]


# mask = ((df['year'] == 2021) &(df['car_code'] ==  4))
# result = int(self.df.loc[mask, (f'{area}', f'Unnamed: {i}_level_1')].iloc[0])
# wprint(mask)



df2 = df[(df['year'] == 2020) & (df['car_code'] == 5)]
print(df2)

df3 = df[(df['year'] == 2021) & (df['car_code'] == 5)]
print(df3)

df4 = df[(df['year'] == 2022) & (df['car_code'] == 5)]
print(df4)

df5 = df[(df['year'] == 2023) & (df['car_code'] == 5)]
print(df5)

df6 = df[(df['year'] == 2024) & (df['car_code'] == 5)]
print(df6)


fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 색상 설정
ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성


plt.plot(df2['area'], df2['total'], color='#e35f62', label=2020)
plt.plot(df3['area'], df3['total'], color="#e99362", label=2021)
plt.plot(df4['area'], df4['total'], color="#D1D13A", label=2022)
plt.plot(df5['area'], df5['total'], color="#61e35f", label=2023)
plt.plot(df6['area'], df6['total'], color="#5f96e3", label=2024)

# plt.fill_between(df2['area'][0:6], df2['area'], df3['area'], color='lightgray', alpha=0.5)

plt.legend(loc=(0.02, 0.75), fontsize=14, frameon=True, shadow=True)
plt.xlabel('지역', labelpad=15)
plt.ylabel('수소차 등록 대수(누적)', labelpad=15)
plt.grid()

# plt.plot(df2['area'], df2['total'], 'r--', df3['area'], df3['total'], 'r--', df4['area'], df4['total'], 'r--', df5['area'],
#           df5['total'], 'r--', df6['area'], df6['total'], 'r--')
plt.title('연도-지역별 수소차 증가 현황',fontsize=20)   ## 타이틀 설정

plt.show()


# fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
# fig.set_facecolor('white') ## 캔버스 색상 설정
# ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성

# ax.plot(df2['area'],df2['total'])
#  ax.plot(df2['area'],df2['total'])
# plt.title('Sales for 10 days',fontsize=20) ## 타이틀 설정
# plt.show()

