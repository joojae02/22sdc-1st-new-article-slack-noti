from .Blog import Blog
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SmdcmartBlog(Blog) :

    def __init__ (self, name, first_page_url) :
        super(SmdcmartBlog, self).__init__(name, first_page_url)

    def open_post_table(self) :
        return self.web_driver.find_element(By.XPATH, '//*[@id="prologue"]/dl')

    def read_title_url_date_from_table(self) : 
        print('read_title_url_date_from_table')
        dd_table = self.open_post_table()
        dd_list = dd_table.find_elements(By.TAG_NAME, 'dd')
        for value in dd_list :
            tag_ul = value.find_element(By.TAG_NAME, 'ul')
            tag_a = tag_ul.find_element(By.TAG_NAME, 'a')
            title = tag_a.get_attribute('text')            
            url = tag_a.get_attribute('href')
            
            date = tag_ul.find_element(By.TAG_NAME,'span')

            self.title_list.append(title)
            self.title_url_date_dic[title] = [url, date.text]

    def access_to_post(self) :
        title = self.find_correct_post()
        # title = "8월 1주차 입고리스트"

        if title is not None :
            self.web_driver.get(self.title_url_date_dic[title][0])
            time.sleep(1)
        else :
            print('해당하는 게시물이 없습니다')

    def check_post_name(self, post_title) :
        if '와인' in post_title :
            return True
        return False

    def find_correct_post(self) :
        for key in self.title_url_date_dic :
            if self.check_post_date(self.title_url_date_dic[key][1]) and self.check_post_name(key) :
                return key
        return None

    def read_content(self) :
        content = self.web_driver.find_element(By.XPATH,'//*[@id="post-view222858485837"]/div/div[2]')
        text_content_list = content.find_elements(By.CLASS_NAME, 'se-component.se-text.se-l-default')
        
        for text_content in text_content_list :
            text_list = text_content.find_elements(By.TAG_NAME, 'span')
            
            for w in text_list :
                self.wine_list.append(w.text)

        