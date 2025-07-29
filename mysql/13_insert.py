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


# sql = "insert into tbl_menu (menu_name, menu_price, category_code, orderable_status) values('허니콤보', 20000, 4, 'y')"    - 직접 값을 넣을때
sql = "insert into tbl_menu (menu_name, menu_price, category_code, orderable_status) values(%s, %s, %s, %s)"                
# %s, %d, %d, %s : 문자/숫자로 생각해서 이렇게 넣으면 안됨. 플레이스 홀더: %s로 사용해야함. just 위치를 잡아주는 것이기떄문에, 갯수와 순서를 맞춰서 넣어줘야함.

values = ("레드콤보", 23000, 4, 'y')    # 위치인자는 갯수 상관없이 시퀀스 형태로 반환 (주로 튜플)

cursor.execute(sql, values)   #sql 명령 구문에 cursor에 담김

#commit 처리 
connection.commit()

print(f'@@@{cursor.rowcount}개의 행 삽입 완료@@@')

# result_rows = cursor.fetchall()   insert 는 반환이 안됨.  

#for row in result_rows :        
#    print(row)

cursor.close()       # cursor 사용 종료 (자원 반납)
connection.close()   # 연결 객체 닫기

# 실행시 : python python-mysql.py  (cmd 창에)
