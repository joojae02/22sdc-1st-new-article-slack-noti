<<<<<<< HEAD
from blogs.JoyangBlog import JoyangBlog

def main() :
    joyang_blog = JoyangBlog('조양', 'https://blog.naver.com/joyangmart')
    
    joyang_blog.open_web_driver()
    joyang_blog.switch_to_frame('mainFrame')
    joyang_blog.open_first_post_table()
    joyang_blog.read_title_url_date_from_table()
    joyang_blog.open_second_next_post_table()
    joyang_blog.read_title_url_date_from_table()
    joyang_blog.print_title_url()
    joyang_blog.access_to_post()
    joyang_blog.read_content()
main()
=======
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManger

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

today_year = datetime.today().year   # 현재 연도 가져오기
today_month = datetime.today().month # 현재 월 가져오기
today_date = datetime.today().day    # 현재 일 가져오기
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

def week_no(y, m, d):
    # 연월일을 입력받아 해당 요일의 주차를 얻는 함수
    def _ymd_to_datetime(y, m, d): # 3
        s = f'{y:04d}-{m:02d}-{d:02d}'
        return datetime.strptime(s, '%Y-%m-%d')

    target_day = _ymd_to_datetime(y, m, d) # 4
    firstday = target_day.replace(day=1) 

    while firstday.weekday() != 0: 
        firstday += timedelta(days=1)
      
    if target_day < firstday: 
        return 0
  
    return (target_day - firstday).days // 7 + 1 

today_week = week_no(today_year, today_month, today_date)
month_week_format = '{month}월 {week}주차'.format(month = today_month, week = today_week)

print(month_week_format)

month_week_format = '8월 1주차'


# n월 n주자 입고리스트 - 
for t in title_list:
    if month_week_format in t :
        
        print(t + ' :' + title_url_dic[t])
        break
    
web_driver.get(title_url_dic[t])
# print(web_driver.text)
time.sleep(3)

# web_driver.switch_to.frame('mainFrame')
wine_table_block = web_driver.find_element(By.XPATH,'//*[@id="SE-a6fd6072-e4ae-41e9-b5ad-946a8fa5de15"]/div/div/blockquote/div[2]')
wine_table_list = wine_table_block.find_elements(By.TAG_NAME, 'p')
for w in wine_table_list:
    print(w.text)

>>>>>>> f4aa72f7561d9f83a30bc7e54608e1382d1bc624
