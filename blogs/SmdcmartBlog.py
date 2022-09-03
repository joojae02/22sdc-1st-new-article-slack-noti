from .Blog import Blog
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SmdcmartBlog(Blog) :

    def __init__ (self, name, first_page_url, db) :
        super(SmdcmartBlog, self).__init__(name, first_page_url, db)
    def save_wine_list(self) :
        self.open_web_driver()
        self.switch_to_frame('mainFrame')
        self.read_title_url_date_from_table()
        self.read_content_posts()
        self.insert_db_title_list()

    def get_post_table(self) :
        return self.web_driver.find_element(By.XPATH, '//*[@id="prologue"]/dl')

    def read_title_url_date_from_table(self) : 
        dd_table = self.get_post_table()
        dd_list = dd_table.find_elements(By.TAG_NAME, 'dd')
        for value in dd_list :
            class_tag_title = value.find_element(By.CLASS_NAME, 'p_title')
            class_tag_date = value.find_element(By.CLASS_NAME, 'p_date')
            tag_a = class_tag_title.find_element(By.TAG_NAME, 'a')
            title = tag_a.get_attribute('text')            
            url = tag_a.get_attribute('href')
            
            date = class_tag_date.find_element(By.TAG_NAME,'span')
            if self.check_post_name(title) :
                self.title_list.append(title)
                if self.db.is_title_not_exist_in_db(title) == 1 :
                    self.not_exist_title_list.append(title)
                self.title_url_date_dic[title] = [url, date.text]
        
    def check_post_name(self, post_title) :
        if '와인' in post_title :
            return True
        return False



        
    

    

        