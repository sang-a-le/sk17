from selenium import webdriver    # 드라이버 연동을 위한 모듈
import time                         
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

path = 'chromedriver.exe'        # 현위치 기준 상대 위치 경로 잡기
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.bmw.co.kr/ko/services/bmw-service-program/wp/faq.html')
time.sleep(1)

search_box = driver.find_element(By.class, 'ds2-accordion ds2-component ds2-tracking-aware ')
print(search_box)