# 정적 페이지 웹 스크래핑 -> requests, beautifulsoup
# 정적 페이지 = 요청한 url에서 응답받은 html을 그대로 사용한 경우
#             (server side rendering)

import requests
from bs4 import BeautifulSoup   # beautifulsoup = class

def web_request(url):
    response = requests.get(url)   
    print(response)                 # reponse [200]
    print(response.status_code)     # 응답코드
    print(response.text)            # html
    return response

url = "https://naver.com"                                       # ../ 가 해당 파일 기준 밖에 있다는 의미 
response = web_request(url)


with open('../html_sample.html', 'r', encoding='utf-8') as f:
    html = f.read()


bs = BeautifulSoup(html, 'html.parser')
#print(bs)
#print(type(bs))

def test_find():
    #find() : tag 하나만 조회. html 태그 및 속성을 dict로 조회 (1개만 조회)   앨래먼트 객체??
    tag = bs.find('li')
    print(tag)
    print(type(tag))

    #find_all() : html 태그 및 속성을 dict로 조회 (전부 다 조회)
    tags = bs.find_all('section', {'id':'section1'})    # 속성을 부여할 땐 딕셔너리로 부여   리스트로 반환
    print(tags)
    print(type(tags))


def test_selector():                             # css 선택자로 줘야함. 
    tag = bs.select_one('section#section2')      # 앨래먼트로 반환
    print(tag)
    print(type(tag))

    tags = bs.select('.section-content')         # result set 으로 반환
    print(tags)
    print(type(tags))


# 실습
#[힌트]
# resultset(시퀀스 형태, 반복문 사용 가능) -> tag(resultset을 반복문해서 하나씩 반환) -> text 속성 : 내용

def get_content1():
    # id가 section2인 section 태그의 후손 li 태그'들'을 추출 - select
    for tag in bs.select('.section2') :   
        tag2 = tag.find_all('li')
        print(tag2)
        print(type(tag2))

# 정답
def get_content1():
    for tag in bs.select('section#section2 li') :    # 옆에 li 를 붙여주면 후손 뽑는 것
    
        for tag in tags:
            print(tag.text)


def get_content2():
    # id가 section1인 section 태그의 자식 h2태그의 '내용', p 태그의 '내용' 출력 (text 속성)
    for tag in bs.select('.section1') :
        tag2 = tag.find('h2')
        tag3 = tag.find('p')
        print(tag.text(tag2))
        print(tag.text(tag3))

# 정답
def get_content2():
    h2_tag = bs.select_one('section#section1 > h2')      # 자료형을 알기때문에 하나만 뽑는다고 함. 
    print(h2_tag.text)

    p_tag = bs.select('section#section1 > p')           # 시퀀스 자료형이라 반복문 사용
    for tag in p_tag:
        print(tag.text)

def get_content3():
    # id가 section1인 section 태그의 자식태그 조회 -> 내용 출력
    # section#section1 -> select() 또는 select_one() 
    # findchildren() : 태그 객체가 가지고 있음. 
    for tag in bs.select('.section1') :

# 정답1
def get_content3():
    section1_tag = bs.select_one('section#section1')
    childeren = section1_tag.findChildren()
    print(childeren)
# deprecationWarning : 점진적으로 없애고 있는 기능으로 사용을 지양해라 

# 정답2
h2_tag = section1_tag.select_one('h2')
p_tags = section1_tag.select('p')
print(h2_tag.text)
print([p_tag.text for p_tag in p_tags])

#test_find()
#test_selector()
#get_content1()
#get_content2()
#get_content3()
