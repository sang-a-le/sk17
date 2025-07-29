import urllib.request   
import json
import mysql.connector


client_id = 'q9QOvesVk6Ae7tIAEIYL'
client_secret = 'S34ChCh8Lf'

text = '소설'
encText = urllib.parse.quote(text)
url = 'https://openapi.naver.com/v1/search/book.json?query=' + encText
request = urllib.request.Request(url)

request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)

response = urllib.request.urlopen(request)     # 오픈api 반환

print(response.getcode())  
response_body = response.read()
print(response_body.decode('utf-8'))

# DB 연결 객체 생성

#json.loads(json)

connection = mysql.connector.connect(
    host = 'localhost',    # mysql 서버 주소 (서버에 올리는 경우 url 주소 넣기)
    user = 'ohgiraffers',    # 사용자 이름
    password = 'ohgiraffers',   # 비밀번호
    database = 'menudb'    # 사용할 데이터베이스(스키마) / DB 바꾸면서 사용 불가능, 지정해서 확인
)  # sql과 연결

if connection.is_connected() : 
    print('@@@mysql 서버에 정상적으로 연결@@') 

cursor = connection.cursor()
a = json.loads(response_body.decode('utf-8'))
print(a)


for b in a['items'] :
    sql = "insert into bookdb(book_number, book_title, book_image, author, publisher, isbn, book_description, pub_date) values (null, %s, %s, %s, %s, %s, %s, %s)"
    values = (b['title'], b['link'], b['image'], b['author'], b['publisher'], b['isbn'], b['description'], b['pubdate'])
    cursor.execute(sql, values) 
    connection.commit()        



print(f'@@@{cursor.rowcount}개의 행 삽입 완료@@@')
cursor.close()       
connection.close()

################# 전체 내용 가져오기

#dick_book = json.loads(response_body)
#total = dict_book['total']
#start_num =1

#for total // display +1
