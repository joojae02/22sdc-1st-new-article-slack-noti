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
        self.chrome_options.binary_location = '/opt/chrome/chrome'

        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument("--single-process")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-dev-tools")
        self.chrome_options.add_argument("--no-zygote")

        # self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--remote-debugging-port=9222")
        self.web_driver = webdriver.Chrome("/opt/chromedriver", options=self.chrome_options)

        self.title_list = []
        self.not_exist_title_list = []
        self.title_content_dic = {}
        self.title_url_date_dic = {}

    def save_wine_list(self) :
        self.open_web_driver()
        self.switch_to_frame('mainFrame')
        self.open_post_table()
        self.read_title_url_date_from_table()
        print(self.title_list)
        self.read_content_posts()
        self.insert_db_title_list()

    def open_post_table(self) :
        self.web_driver.find_element(By.CLASS_NAME, 'pcol2._toggleTopList._returnFalse').click()
        time.sleep(1)

    def read_title_url_date_from_table(self) : 
        table = self.web_driver.find_element(By.XPATH, '//*[@id="listTopForm"]/table') 
        tbody = table.find_element(By.TAG_NAME,'tbody')
        rows = tbody.find_elements(By.TAG_NAME,'tr')
        for value in rows:
            td_body = value.find_elements(By.TAG_NAME,'td')
            title = td_body[0].find_element(By.TAG_NAME,'a')
            date = td_body[1].find_element(By.TAG_NAME,'span')
            url = title.get_attribute('href')
            if self.check_post_name(title.text) :
                self.title_list.append(title.text)
                if self.db.is_title_not_exist_in_db(title.text) == 1 :
                    self.not_exist_title_list.append(title.text)
                self.title_url_date_dic[title.text] = [url, date.text]
        

     
    def check_post_name(self, post_title) :
        if '입고리스트' in post_title or '입고 리스트' in post_title :
            return True
        return False
    
    

    def open_second_next_post_table(self) :
        self.web_driver.find_element(By.XPATH,'//*[@id="toplistWrapper"]/div[2]/div/a[1]').click() # 다음 목록 열기
        time.sleep(1)
    

    
    def open_web_driver(self):
        print(self.first_page_url)
        self.web_driver.get(self.first_page_url)        



    def switch_to_frame(self, frame_name) :
        self.web_driver.switch_to.frame(frame_name)
        print("switch_to_frame")

   

    def find_correct_post(self) :
        for key in self.title_url_date_dic :
            if self.check_post_name(key) :
                return key
        return None

    
    
    def read_content_posts(self) :
        for title in self.not_exist_title_list :
            print(title + " : " + self.title_url_date_dic[title][0])
            self.web_driver.get(self.title_url_date_dic[title][0])
            try:
                element = WebDriverWait(self.web_driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'se-main-container'))
                )
                self.title_content_dic[title] = self.list_to_str(self.read_content())
            except TimeoutException:
                print("timeout")
            

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
    
