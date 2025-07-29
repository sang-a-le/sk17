import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve    # 사진 저장
from datetime import datetime 

# 스크랩한 뉴스 정보를 담을 newsentry class 생성 (쉽게 하기 위함.)
class NewsEntry : 
    def __init__(self, title, href, img_path):
        self.title = title
        self.href = href
        self.img_path = img_path

    def __repr__(self):           # 보여주는 형태를 변형
        return f'NewsEntry<title={self.title}, href={self.href}>'
    

#1. requests -> url 요청
keyword = input('뉴스 검색 키워드 입력: ')
url = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"    #입력받은 값을 검색어로 반환 / 뒤에 %ㅁ%ㄹ%d 하던 부분은 한글 검색어가 들어가는 부분이라 그부분을 f스트링으로 변환

response = requests.get(url)   #url 받기 


# 2. html 응답 (페이지 받아옴)
html = response.text     #url 문자열로 받기


# 3. beautifulsoup 객체 생성 (html 파싱을 통해)
bs = BeautifulSoup(html, 'html.parser')   #html 문자열 파싱해서 객체로 받기 

#news_contents_box = bs.select_one('.fds-news-item-list-tab')  # 요소 확인하기 
#print(news_contents)
#print(news_contents[0])


# 4. 뉴스 박스 아이템 받기
news_contents = bs.select('.fds-news-item-list-tab > div')   # 한 기사당 div 태그로 분리 되어있음. 

# newsentry 객체를 담을 배열 초기화
news_list = []

# 결과 구조 만들기 
for idx, news_content in enumerate(news_contents):
    title_tag = news_content.select_one('span.sds-comps-text-type-headline1')
    href_tag = title_tag.find_parent('a')   #부모요소 찾기 
    img_tag = news_content.find_all('img')[1]
    
    title = title_tag.text
    href = href_tag['href']
    img_path = ''
    

    # 이미지 경로 추출 + 이미지 저장
    if img_tag.has_attr('src'):
        img_path = img_tag['src']

        img_dir = 'images'
        file_name = datetime.now().strftime('%y%m%d_%H%M%S_') + str(idx + 1) + '.jpg'
        urlretrieve(img_path, f'{img_dir}/{file_name}')
    
    news_entry = NewsEntry(title, href, img_path)   # 객체 만들기
    news_list.append(news_entry)       

# 결과 출력
for news in news_list : 
    print(news)

