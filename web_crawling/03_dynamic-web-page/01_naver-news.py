# 동적 페이지 웹 크롤링 -> selenium
# 동적 페이지 : 요청한 URL에서 응답받은 HTML 안의 JS 를 실행해 HTML을 새로 만든 경우 (Client Side Rendering)

# +)
# ssr : 정적 크롤링 ( html 반환)
# csr : 동적 크롤링 (요구 시 자바 스크립트 반환)

# Selenium
# - 인증을 요구하는 특정 웹 페이지의 데이터 스크랩
# - 무한 댓글 스크랩
# - 브라우저용 매크로 
from selenium import webdriver    # 드라이버 연동을 위한 모듈
import time                         
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   #키보드 입력을 도와주는 모듈

########## 순서
# 1. chrome 브라우저 실행
# 2. 특정 url 접근
# 3. 데이터 가져오기
# 4. 브라우저 종료 (드라이버 종료)  -- 브라우저를 실행하는것이 드라이버 (동일한 말임)

# 1. chrome 브라우저 실행
# C:\web_crawling\03_dynamic-web-page 위치로 chromedriver 이동 (스크린샷 참고)
path = 'chromedriver.exe'        # 현위치 기준 상대 위치 경로 잡기
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

# 2. 특정 url 접근
#driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&ssc=tab.news.all&query=%ED%81%AC%EB%A1%A4%EB%A7%81&oquery=%EB%B2%85%EC%8A%A4&tqi=jb364lqptbNssfjTH3CssssstTs-423464&ackey=5spv0po9")
driver.get('https://naver.com')
time.sleep(1)   #1초 동안 기다려라. selenium 이 url에 접근 시 완료되는 것 기다리기

# - 검색어 입력 및 검색
search_box = driver.find_element(By.ID, 'query')
search_box.send_keys('크롤링')    # 인자로 넣어준걸 그대로 전달
search_box.send_keys(Keys.RETURN)   #enter를 누르는 것과 동일하게 작동
time.sleep(1)

# - 뉴스탭 이동
next_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[2]/div[2]/a/span')   # 뉴스 키를 누를 때의 주소 
next_btn.click()
time.sleep(1)

news_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[9]/a')   # 뉴스 키를 누를 때의 주소 
news_btn.click()
time.sleep(1)

# - 스크롤 처리 (end 키로 뉴스 계속 생성)
'''
body = driver.find_element(By.TAG_NAME, 'body')  # body : 전체 영역 에서 
body.send_keys(Keys.END)
time.sleep(1)
'''
for _ in range(5) :            # 무한 스크롤 가능
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    time.sleep(1)


# 3. 데이터 가져오기
news_contents_elems = driver.find_elements(By.CSS_SELECTOR, 'span.sds-comps-text-type-headline1')   
                 #by로 요소 설계 위함. css 선택자 형식이어야함. 대문자로만 이루어져 있으면, 상수(변경x)
for news_contents_elem in news_contents_elems :
    parent = news_contents_elem.find_element(By.XPATH, '..')    # .. : 상위 / span 태그와 a 태그를 잡음 (각각 parent, news)
    title = news_contents_elem.text
    href = parent.get_attribute('href')
    print(title, '|', href)

# 4. 브라우저 종료 (드라이버 종료)
driver.quit()



