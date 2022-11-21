from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import os 
import urllib.request
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')

service = Service(ChromeDriverManager().install())
web_driver = webdriver.Chrome(service = service, options=chrome_options)


wine_kor_name = [] 
wine_en_name = []
wine_type = []
wine_winery = []
wine_winery_en = []

wine_country = []
wine_region = []
wine_grape = []

wine_grade = []
wine_win = []
wine_alc = []
wine_size = []
wine_body = []
wine_sweetness = []
wine_acid= []
wine_tannin = []
wine_color = []
wine_temp = []
wine_nose = []
wine_taste = []
wine_paring = []

wine_desc = []
winery_desc = []

wine_no = []
wine_image_list = []
wine_dec = []
num = 463
for i in range(1, 2) :
    url_list = []
    time.sleep(3)

    web_driver.get('https://redwinenjy.winehero.co.kr/shop/item.php?it_id=1624923174')
    # web_driver.get('https://redwinenjy.winehero.co.kr/shop/search.php?qname=1&qexplan=1&qid=1&qbasic=1&qfrom=1000&qto=300000&qcaid=&q=&qsort=&qorder=&page=' + str(i))
    # table = web_driver.find_element(By.XPATH, '//*[@id="sct_wrap"]')
    '''
    div_list = table.find_elements(By.CLASS_NAME, 'product_list_box')
    
    for div in div_list :
        a_list = div.find_element(By.TAG_NAME, 'ul')
        u = a_list.get_attribute('onclick')
        url = u.split('\'')
        url_list.append(url[1])
'''
print(web_driver.title)
print(web_driver.page_source)
'''    for url in url_list :
        web_driver.get(url)
        wine_table = web_driver.find_element(By.XPATH, '//*[@id="about"]/div[2]/div[4]/div[3]/table/tbody')
        td_list = wine_table.find_elements(By.CLASS_NAME, 'board_text')

        wine_num = 'jh_' + str(num).zfill(6)
        wine_no.append(wine_num)

        wine_en_name.append(td_list[0].text)
        wine_kor_name.append(td_list[1].text)
        wine_win.append(td_list[2].text)
        tmp = td_list[3].text
        wwinery = tmp.replace(')','').split('(')
        wine_winery_en.append(wwinery[0])
        if len(wwinery) != 1 :
            wine_winery.append(wwinery[1])
        else :
            wine_winery.append('')

        wine_country.append(td_list[4].text)

        wine_type.append(td_list[5].text)
        
        wine_grape.append(td_list[6].text)

        wine_alc.append(td_list[7].text)
        wine_paring.append(td_list[8].text.replace(', ', '||'))
        num_list = []

        for i in range(9,13) :
            im_list = td_list[i].find_elements(By.TAG_NAME, 'img')
            start = 0
            for im in im_list :
                src = im.get_attribute('src')
                if 'on' in src or 'hf' in src :
                    start = start + 1
            if start == 0 :
                start = 1
            num_list.append(start)
        
        wine_sweetness.append(num_list[0])
        wine_acid.append(num_list[1])
        wine_body.append(num_list[2])
        wine_tannin.append(num_list[3])

        body_table = web_driver.find_element(By.XPATH, '//*[@id="about"]/div[2]/div[4]/div[4]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody')
        txt_desc = body_table.text.replace('\n', ' ')
        txt_desc = txt_desc.replace('DESCRIPTION', '')
        txt_d = txt_desc.split('TASTING NOTE')
        wine_desc.append(txt_d[0])
        if len(txt_d) != 1 :
            winery_desc.append(txt_d[1])
        else :
            winery_desc.append('')
        num += 1
        wine_image_list.append(wine_num+'_org.png')

        image_url = web_driver.find_element(By.XPATH, '//*[@id="about"]/div[2]/div[4]/div[2]/table/tbody/tr/td/img').get_attribute('src')
    

        image_name = '/mnt/c/Users/jake0/Desktop/Study/22sdc-1st-new-article-slack-noti/img/jh_' + str(num).zfill(6) + '_org.png'
        urllib.request.urlretrieve(image_url, image_name)

        

print(len(wine_num))
print(len(wine_sweetness))
print(len(wine_acid))
print(len(wine_tannin))

# 워크북(엑셀파일)을 새로 만듭니다.

'''