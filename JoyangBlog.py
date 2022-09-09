from Blog import Blog
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class JoyangBlog(Blog) :
    ''' 조양마트 블로그  '''

    def __init__ (self, name, first_page_url, db) :
        super(JoyangBlog, self).__init__(name, first_page_url, db)

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
    


