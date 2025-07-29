# from read_xls import table_reader
from xls2db import XLS2DB
from crawling import start

xls_files = {
    '2020': 'raw_files/2020년_12월_자동차_등록자료_통계.xlsx',
    '2021': 'raw_files/2021년_12월_자동차_등록자료_통계.xlsx',
    '2022': 'raw_files/2022년_12월_자동차_등록자료_통계.xlsx',
    '2023': 'raw_files/2023년_12월_자동차_등록자료_통계.xlsx',
    '2024': 'raw_files/2024년_12월_자동차_등록자료_통계.xlsx',
}

header = [2, 3]
sheet_name = 9
ev, hd = start()

generator = XLS2DB()

# for year, xls_path in xls_files.items():
#    print(year)
#    is_nan = True if int(year) <= 2022 else False
#    generator.make_db(year, xls_path, header, sheet_name, is_nan=is_nan)

generator.make_subsidy(ev, hd)
generator.close()