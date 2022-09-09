from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Blog :

    def __init__ (self, name, first_page_url, db) :
        self.name = name
        self.db = db
        self.first_page_url = first_page_url
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--window-size=1280x1696")
        self.chrome_options.add_argument("--single-process")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-dev-tools")
        self.chrome_options.add_argument("--no-zygote")
        # chrome_options.add_argument('--user-data-dir=/tmp/chrome-user-data')
        self.chrome_options.add_argument("--remote-debugging-port=9222")

        # self.chrome_options.binary_location = '/root/chrome-linux/chrome'
        # self.web_driver = webdriver.Chrome("/root/chromedriver", options = self.chrome_options)
        # chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.0 Safari/537.36')
        self.chrome_options.binary_location = '/opt/chrome/chrome'
        self.web_driver = webdriver.Chrome("/opt/chromedriver", options=self.chrome_options)

        self.title_list = []
        self.not_exist_title_list = []
        self.title_content_dic = {}
        self.title_url_date_dic = {}


    
    def open_web_driver(self):
        print(self.first_page_url)
        self.web_driver.get(self.first_page_url)        



    def switch_to_frame(self, frame_name) :
        self.web_driver.switch_to.frame(frame_name)
        print("switch_to_frame")

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

    
    
    def read_content_posts(self) :
        for title in self.not_exist_title_list :
            print(title + " : " + self.title_url_date_dic[title][0])
            self.web_driver.get(self.title_url_date_dic[title][0])
            element = WebDriverWait(self.web_driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'se-main-container'))
            )
            self.title_content_dic[title] = self.list_to_str(self.read_content())


    def list_to_str(self, list) :
        text = ''
        for s in list :
            text += s + '\n'
        return text


    def insert_db_title_list(self) :
        reversed_title_list = reversed(self.not_exist_title_list)
        for title in reversed_title_list :
            tmp = self.db.insert_db(title, self.title_content_dic[title], self.name , self.title_url_date_dic[title][0])


    def get_title_list (self) :
        return self.title_list
    def get_title_content_dic (self) :
        return self.title_content_dic
    def get_name (self) :
        return self.name
    def get_title_url_date_dic (self) :
        return self.title_url_date_dic
    def get_not_exist_title_list(self) :
        return self.not_exist_title_list
    
