from .Blog import Blog
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SmdcmartBlog(Blog) :

    def __init__ (self, name, first_page_url) :
        super(SmdcmartBlog, self).__init__(name, first_page_url)

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

            self.title_list.append(title)
            self.title_url_date_dic[title] = [url, date.text]

    def access_to_post(self) :
        self.content_title = self.find_correct_post()
        if self.content_title is not None :
            self.web_driver.get(self.title_url_date_dic[self.content_title][0])
            time.sleep(1)
        else :
            print('해당하는 게시물이 없습니다')

    def check_post_name(self, post_title) :
        if '와인' in post_title :
            return True
        return False

    def save_wine_list(self) :
        self.open_web_driver()
        self.switch_to_frame('mainFrame')
        self.read_title_url_date_from_table()
        self.access_to_post()
        self.read_content()
    
        
    

    

        