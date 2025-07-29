# 메뉴코드가 10번인 메뉴 삭세 
# 메뉴코드는 변수에 담아서 사용

import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',    # mysql 서버 주소 (서버에 올리는 경우 url 주소 넣기)
    user = 'ohgiraffers',    # 사용자 이름
    password = 'ohgiraffers',   # 비밀번호
    database = 'menudb'    # 사용할 데이터베이스(스키마) / DB 바꾸면서 사용 불가능, 지정해서 확인
) 

cursor = connection.cursor()

sql = "delete from tbl_menu where menu_code = 10"

#commit 처리 
connection.commit()

print(f'@@@{cursor.rowcount}개의 행 삭제 완료@@@')

# result_rows = cursor.fetchall()   insert 는 반환이 안됨.  

#for row in result_rows :        
#    print(row)

cursor.close()       # cursor 사용 종료 (자원 반납)
connection.close()   # 연결 객체 닫기