import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',    # mysql 서버 주소 (서버에 올리는 경우 url 주소 넣기)
    user = 'ohgiraffers',    # 사용자 이름
    password = 'ohgiraffers',   # 비밀번호
    database = 'menudb'    # 사용할 데이터베이스(스키마) / DB 바꾸면서 사용 불가능, 지정해서 확인
)  # sql과 연결

if connection.is_connected() : 
    print('@@@mysql 서버에 정상적으로 연결@@')


cursor = connection.cursor()   # 실행 구문 받아오기 


sql = 'select * from tbl_menu'      ########## select 구문

cursor.execute(sql)   #sql 명령 구문에 cursor에 담김

result_rows = cursor.fetchall()   #수행하고 가져온 결과를 시퀀스 형태로 result_rows에 저장 

for row in result_rows :        #시퀀스 형태이기 때문에 반복문 이용해서 한 문장 씩 반환
    print(row)

cursor.close()       # cursor 사용 종료 (자원 반납)
connection.close()   # 연결 객체 닫기

# 실행시 : python python-mysql.py  (cmd 창에)
