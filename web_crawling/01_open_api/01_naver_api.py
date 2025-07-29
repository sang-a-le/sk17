import urllib.request     

client_id = 'q9QOvesVk6Ae7tIAEIYL'
client_secret = 'S34ChCh8Lf'

text = 'AI'         # 검색어
encText = urllib.parse.quote(text)  #urllib의 parse 함수는 해당 text를 인토딩해서 반환함. 
 
url = 'https://openapi.naver.com/v1/search/news.json?query=' + encText    #인코딩 값(쿼리값) 연결

request = urllib.request.Request(url)      #인스턴스가 만들어짐

# 네이버 예시는 c언어로 작성되어 있음. 해더 설정
request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)       #secret 키 보호를 위해 함수로 설정

response = urllib.request.urlopen(request)     # 오픈api 반환

print(response.getcode())  # http 응답 상태코드 반환 : 200 은 성공. 예외처리에 사용
#print(response.read())   # 응답 내용, 응답 코드 반환. 응답에서 확인 가능. but utf-8 형태로 반환되어 확인 불가능
response_body = response.read()
print(response_body.decode('utf-8'))  #한글로 해석. 네이버 '응답'에서 해당 라벨의 뜻 판명 가능

