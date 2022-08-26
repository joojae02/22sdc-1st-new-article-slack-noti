from .Blog import Blog
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class JoyangBlog(Blog) :
    ''' 조양마트 블로그  '''

    def __init__ (self, name, first_page_url) :
        super(JoyangBlog, self).__init__(name, first_page_url)
        


    def open_first_post_table(self) :
        self.web_driver.find_element(By.CLASS_NAME, 'pcol2._toggleTopList._returnFalse').click()
        time.sleep(1)

    def read_title_url_date_from_table(self) : 
        table = self.web_driver.find_element(By.XPATH, '//*[@id="listTopForm"]/table') 
        tbody = table.find_element(By.TAG_NAME,'tbody')
        rows = tbody.find_elements(By.TAG_NAME,'tr')
        for index, value in enumerate(rows):
            td_body = value.find_elements(By.TAG_NAME,'td')
            title = td_body[0].find_element(By.TAG_NAME,'a')
            date = td_body[1].find_element(By.TAG_NAME,'span')
            
            url = title.get_attribute('href')
            self.title_list.append(title.text)
            self.title_url_date_dic[title.text] = [url, date.text]

    def open_second_next_post_table(self) :
        self.web_driver.find_element(By.XPATH,'//*[@id="toplistWrapper"]/div[2]/div/a[1]').click() # 다음 목록 열기
        time.sleep(1)
     
    def print_title_url(self) :
        print(self.title_url_date_dic)

    def access_to_post(self) :
        title = self.find_correct_post()
        title = "8월 1주차 입고리스트"
        if title is not None :
            self.web_driver.get(self.title_url_date_dic[title][0])
            time.sleep(1)
        else :
            print('해당하는 게시물이 없습니다')

    def check_post_name(self, post_title) :
        if '입고리스트' in post_title or '입고 리스트' in post_title :
            return True

    def find_correct_post(self) :
        for key in self.title_url_date_dic :
            if self.check_post_date(self.title_url_date_dic[key][1]) and self.check_post_name(key) :
                return key
        return None

    def read_content(self) :
        self.wine_list = []
        table_block = self.web_driver.find_element(By.XPATH,'//*[@id="SE-a6fd6072-e4ae-41e9-b5ad-946a8fa5de15"]/div/div/blockquote/div[2]')
        table_list = table_block.find_elements(By.TAG_NAME, 'p')
        for w in table_list :
            self.wine_list.append(w.text)
        print(self.wine_list)


