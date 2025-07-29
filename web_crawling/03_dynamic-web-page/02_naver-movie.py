# 네이버 현재 상영 영화
# 제목 & 링크 따오기 

# 1. Chrome 브라우저 실행
# 2. naver에 현재상영영화 검색
# 3. 영화 영역 탐색
  # 심화 : 다음 페이지도 가지고 오기
# 4. 영화 제목과 url 출력
  # 심화 : 이미지도 가지고 오기 
# 5. 드라이버 종료

from selenium import webdriver    # 드라이버 연동을 위한 모듈
import time                         
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   #키보드 입력을 도와주는 모듈

path = 'chromedriver.exe'        
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

driver.get('https://naver.com')
time.sleep(1)

search_box = driver.find_element(By.ID, 'query')
search_box.send_keys('현재상영영화')    
search_box.send_keys(Keys.RETURN)  
time.sleep(1)

next_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[2]/div[2]/a/span')   # 뉴스 키를 누를 때의 주소 
next_btn.click()
time.sleep(1)

this_text _text

movie_contents_elems = driver.find_elements(By.CSS_SELECTOR, 'this_text._text')   

for movie_contents_elem in movie_contents_elems :
    parent = movie_contents_elem.find_element(By.XPATH, '..')    # .. : 상위 / span 태그와 a 태그를 잡음 (각각 parent, news)
    title = news_contents_elem.text
    href = parent.get_attribute('href')
    print(title, '|', href)