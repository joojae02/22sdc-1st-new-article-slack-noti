from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Blog :
    ''' Blog 상위 클래스 '''

    today_date = datetime.today()
    today_week = 0
    chrome_options = webdriver.ChromeOptions()
    

    def __init__ (self, name, first_page_url) :
        self.name = name
        self.first_page_url = first_page_url
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        print(self.name)
        self.web_driver = webdriver.Chrome(service = Service("/mnt/c/Users/jake0/Desktop/Study/22sdc-1st-new-article-slack-noti/chromedriver"),options=self.chrome_options)
        self.title_list = []
        self.title_url_date_dic = {}
        self.wine_list = []


    def open_web_driver(self):
        self.web_driver.get(self.first_page_url)
        time.sleep(3)

    def switch_to_frame(self, frame_name) :
        self.web_driver.switch_to.frame(frame_name)

    def print_date(self) :
        month_week_format = '{month}월 {date}일'.format(month = self.today_month, date = self.today_date)
        print(month_week_format)

    def check_post_date(self, post_date):
        if '시간' in post_date :
            return True
        date_before = post_date.replace(' ', '')
        date = date_before.split('.')
        post_datetime = datetime(int(date[0]),int(date[1]),int(date[2]))
        post_after_7 = post_datetime + timedelta(days = 7)
        if post_datetime <= self.today_date and post_after_7 > self.today_date :
            return True
        else :
            return False

    def print_title_url(self) :
        print(self.title_url_date_dic)