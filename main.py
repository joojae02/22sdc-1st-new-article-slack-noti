from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManger

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 조양마트
# 상단 목록 열기
# 목록 1page 2page 요소 title과 url 읽기
# title이 기간에 맞는 할인 리스트일 경우 접속 후
# 할인 리스트 읽기

web_driver = webdriver.Chrome(service = Service("/mnt/c/Users/jake0/Desktop/Study/22sdc-1st-new-article-slack-noti/chromedriver"),options=chrome_options)

url = 'https://blog.naver.com/joyangmart'
web_driver.get(url)
time.sleep(5)

title_list = []
title_url_dic = {}

web_driver.switch_to.frame('mainFrame')

# 상단 목록 열기
web_driver.find_element(By.CLASS_NAME, 'pcol2._toggleTopList._returnFalse').click()
time.sleep(1)

# 목록 title, url 읽어 저장
# title_list : title 저장 리스트
# title_url_dic : key = title , value = url 인 딕셔너리
def get_title_url_from_table(driver) : 
    global title_list
    global title_url_dic
    table = driver.find_element(By.XPATH, '//*[@id="listTopForm"]/table') 
    # table = driver.find_element(By.CLASS_NAME, 'blog2_list.blog2_categorylist') //

    tbody = table.find_element(By.TAG_NAME,'tbody')
    rows = tbody.find_elements(By.TAG_NAME,'tr')


    for index, value in enumerate(rows):
        td_body = value.find_element(By.TAG_NAME,'td')
        title = td_body.find_element(By.TAG_NAME,'a')
        url = title.get_attribute('href')
        print(title.text + " : " + url + "\n")
        title_list.append(title.text)
        title_url_dic[title.text] = url


get_title_url_from_table(web_driver)# 첫번째 목록 읽기
time.sleep(1)

web_driver.find_element(By.XPATH,'//*[@id="toplistWrapper"]/div[2]/div/a[1]').click() # 다음 목록 열기
time.sleep(1)

get_title_url_from_table(web_driver) # 두번째 목록 읽기

print(title_url_dic)


