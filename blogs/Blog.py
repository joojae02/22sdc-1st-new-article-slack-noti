from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from db import DB

class Blog :
    
    chrome_options = webdriver.ChromeOptions()
    
    def __init__ (self, name, first_page_url, db) :
        self.name = name
        self.db = db
        self.first_page_url = first_page_url
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.binary_location= '/usr/bin/google-chrome'
        print(self.name)
        self.web_driver = webdriver.Chrome(service = Service("/mnt/c/Users/jake0/Desktop/Study/22sdc-1st-new-article-slack-noti/chromedriver"),options=self.chrome_options)
        self.title_list = []
        self.title_content_dic = {}
        self.title_url_date_dic = {}
        self.wine_list = []
        self.content_title = ''

    def get_wine_list(self) :
        return self.wine_list
    
    def open_web_driver(self):
        self.web_driver.get(self.first_page_url)
        time.sleep(1)

    def switch_to_frame(self, frame_name) :
        self.web_driver.switch_to.frame(frame_name)


    def read_content(self) :
        content = self.web_driver.find_element(By.CLASS_NAME, 'se-main-container')
        text_content_list = content.find_elements(By.CLASS_NAME, 'se-component.se-quotation.se-l-quotation_underline')
        text_content_list.extend(content.find_elements(By.CLASS_NAME, 'se-component.se-quotation.se-l-default'))
        text_content_list.extend(content.find_elements(By.CLASS_NAME, 'se-component.se-text.se-l-default'))
        tmp_list = []
        for text_content in text_content_list :
            text_list = text_content.find_elements(By.TAG_NAME, 'span')
            for w in text_list :
                tmp_list.append(w.text)

        return tmp_list

    def find_correct_post(self) :
        for key in self.title_url_date_dic :
            if self.check_post_name(key) :
                return key
        return None

    def get_content_title (self) :
        return self.content_title

    def print_wine_list(self) :
        print(self.wine_list)
    
    def read_content_posts(self) :
        for title in self.title_list :
            self.web_driver.get(self.title_url_date_dic[title][0])
            time.sleep(1)
            self.title_content_dic[title] = self.list_to_str(self.read_content())

    def access_to_post(self) :
        self.content_title = self.find_correct_post()
        if self.content_title is not None :
            self.web_driver.get(self.title_url_date_dic[self.content_title][0])
            time.sleep(1)
    
    def list_to_str(self, list) :
        text = ''
        for s in list :
            text += s + '\n'
        return text
    def set_content_title () :
        self.content_title = self.title_list[0]

    def insert_db_title_list(self) :
        reversed_title_list = reversed(self.title_list)
        for title in reversed_title_list :
            self.db.insert_db(title, self.title_content_dic[title], self.name , self.title_url_date_dic[title][0])

    def select_db_title_content(self) :