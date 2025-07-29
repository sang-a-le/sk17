from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time


def start():
    # 1. Chrome 브라우저 실행
    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=service)

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    # # 전기차 보조금 크롤링

    # ###################################### 2020 ############################################
    main_window = driver.window_handles[0]
    driver.get('https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do')
    time.sleep(1)

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2020")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    time.sleep(0.5)
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_ev_2020 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_ev_2020[region] = None # 데이터 없으면 None 처리
            continue
        
        col3_values = []
        col4_values = []
        
        for row in rows:
            try:
                val3 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val4 = float(row[4].replace(',', ''))
                col3_values.append(val3)
                col4_values.append(val4)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg3 = sum(col3_values) / len(col3_values) if col3_values else None
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        
        region_ev_2020[region] = int(avg3)

    # 결과 출력
    for region, avgs in region_ev_2020.items():
        print(f"region_ev_2020 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)

    ###################################### 2021 ############################################

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2021")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_ev_2021 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_ev_2021[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_ev_2021[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_ev_2021.items():
        print(f" region_ev_2021 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)


    ###################################### 2022 ############################################

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2022")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_ev_2022 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_ev_2022[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_ev_2022[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_ev_2022.items():
        print(f"region_ev_2022 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)


    ###################################### 2023 ############################################

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2023")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_ev_2023 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_ev_2023[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_ev_2023[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_ev_2023.items():
        print(f"region_ev_2023 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)


    ###################################### 2024 ############################################

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2024")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_ev_2024 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_ev_2024[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_ev_2024[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_ev_2024.items():
        print(f"region_ev_2024 {region}: ", avgs)

    driver.quit()


    # 수소차 크롤링

    ###################################### 2020 ############################################
    print('############### 수소차 크롤링 #############')
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=service)  # 새 드라이버 시작
    driver.get('https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do')
    time.sleep(1)

    main_window = driver.current_window_handle

    button = driver.find_element(By.XPATH, '//*[@id="editForm"]/div[1]/div/div[1]/table/tbody/tr[1]/td/label[3]')  # 수소차 버튼
    button.click()
    time.sleep(1)

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2020")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_hd_2020 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_hd_2020[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_hd_2020[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_hd_2020.items():
        print(f"region_hd_2020 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)

    ###################################### 2021 ############################################
    print('############### 수소차 크롤링 #############')

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2021")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_hd_2021 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_hd_2021[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_hd_2021[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_hd_2021.items():
        print(f"region_hd_2021 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)

    ###################################### 2022 ############################################
    print('############### 수소차 크롤링 #############')

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2022")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_hd_2022 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_hd_2022[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_hd_2022[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_hd_2022.items():
        print(f"region_hd_2022 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)

    ###################################### 2023 ############################################
    print('############### 수소차 크롤링 #############')

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2023")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_hd_2023 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_hd_2023[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_hd_2023[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_hd_2023.items():
        print(f"region_hd_2023 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)

    ###################################### 2024 ############################################
    print('############### 수소차 크롤링 #############')

    button = driver.find_element(By.XPATH, '//*[@id="year1"]')  # 년도 설정
    select_element = driver.find_element(By.ID, "year1")
    select = Select(select_element)
    select.select_by_value("2024")

    button = driver.find_element(By.XPATH, '//*[@id="btnLocalCarPrc"]')  # 지자체 보조금 버튼
    button.click()

    # 팝업이 뜨는 것을 기다리거나, 새 창을 기다림
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    tbody = driver.find_element(By.CSS_SELECTOR, 'body > form > div > table > tbody')

    # 5. tbody 안의 정보 출력
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
            '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    region_dict = {region: [] for region in regions}

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        region = cols[0].text  # 첫번째 열이 지역명이라고 가정
        if region in regions:
            # 지역별로 행의 텍스트 리스트 저장
            row_data = [col.text for col in cols]  
            region_dict[region].append(row_data)

    print(region_dict.keys())

    region_hd_2024 = {}
    for region, rows in region_dict.items():
        if len(rows) == 0:
            region_hd_2024[region] = None  # 데이터 없으면 None 처리
            continue
        
        col4_values = []
        col5_values = []
        
        for row in rows:
            try:
                val4 = float(row[3].replace(',', ''))  # 천단위 콤마 제거 후 숫자 변환
                val5 = float(row[4].replace(',', ''))
                col4_values.append(val4)
                col5_values.append(val5)
            except (ValueError, IndexError):
                # 데이터 이상 시 무시하거나 로그 출력 가능
                pass
        
        avg4 = sum(col4_values) / len(col4_values) if col4_values else None
        avg5 = sum(col5_values) / len(col5_values) if col5_values else None
        
        region_hd_2024[region] = int(avg4)

    # 결과 출력
    for region, avgs in region_hd_2024.items():
        print(f"region_hd_2024 {region}: ", avgs)
    driver.switch_to.window(main_window)
    driver.switch_to.window(driver.window_handles[1])
    driver.close() 
    driver.switch_to.window(main_window)

    ev = [region_ev_2020, region_ev_2021, region_ev_2022, region_ev_2023, region_ev_2024]
    hd = [region_hd_2020, region_hd_2021, region_hd_2022, region_hd_2023, region_hd_2024]

    return ev, hd