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

service = Service(ChromeDriverManager().install())
web_driver = webdriver.Chrome(service = service, options=chrome_options)


main_url = 'http://www.avecwine.co.kr/'

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

wine_size = []
wine_body = []
wine_sweetness = []
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
num = 321

for i in range(1, 5) :
    
    url_list = []

    web_driver.get('https://zasperowine.com/?swoof=1&post_type=product&paged=1&paged=' + str(i))
    table = web_driver.find_element(By.XPATH, '//*[@id="woof_results_by_ajax"]/ul')
    li_list = table.find_elements(By.TAG_NAME, 'li')
    
    for a in li_list :
        a_list = a.find_element(By.TAG_NAME, 'a')
        url_list.append(a_list.get_attribute('href'))


    for url in url_list :
        web_driver.get(url)
        wine_table = web_driver.find_element(By.XPATH, '//*[@id="product-665"]')
        kor_name = wine_table.find_element(By.XPATH, '//*[@id="product-665"]/div[2]/h1').text
        names = kor_name.split('\n')
        kor_name = names[0] + ' ' + names[1]
        en_name = wine_table.find_element(By.XPATH, '//*[@id="product-665"]/div[2]/div/p').text
        wine_en_name.append(en_name)
        wine_kor_name.append(kor_name)
        
        view_desc = web_driver.find_element(By.XPATH, '//*[@id="product-663"]/div[2]/div/table/tbody')
        
        li_list = view_desc.find_elements(By.TAG_NAME, 'tr')
        
        for i in li_list :
            
        wine_type.append(li_list[0].text.replace('타입',''))


        wine_winery_en.append(li_list[0].text.replace('와이너리',''))
        wine_country.append(li_list[1].text.replace('생산국',''))
        wine_region.append(li_list[2].text.replace('생산지역',''))
        wine_grape.append(li_list[4].text.replace('포도품종',''))
        wine_size.append(li_list[5].text.replace('용량',''))
        wine_temp.append(li_list[6].text.replace('음용온도',''))

        '''body_table = web_driver.find_element(By.XPATH, '//*[@id="wine_view_wrap"]/div[2]/div[1]/div')
        li_list = body_table.find_elements(By.CLASS_NAME, 'on')
        wine_body.append(li_list[len(li_list) - 1].text)

        body_table = web_driver.find_element(By.XPATH, '//*[@id="wine_view_wrap"]/div[2]/div[2]/div')
        li_list = body_table.find_elements(By.CLASS_NAME, 'on')
        wine_sweetness.append(li_list[len(li_list) - 1].text)'''
        
        body_table = web_driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]')
        txt_desc = body_table.find_element(By.CLASS_NAME, 'txt_desc')
        wine_desc.append(txt_desc.text.replace('\n',''))
        body_table = web_driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[2]/div[4]')
        txt_desc = body_table.find_element(By.CLASS_NAME, 'txt_desc')
        winery_desc.append(txt_desc.text.replace('\n',''))

        # 사진
        image_url = web_driver.find_element(By.XPATH, '//*[@id="product-665"]/div[1]/figure/div/a/img').get_attribute('src')

        wine_num = 'jh_' + str(num).zfill(6)
        wine_no.append(wine_num)
        image_name = '/mnt/c/Users/jake0/Desktop/Study/22sdc-1st-new-article-slack-noti/mervin/img/jh_' + str(num).zfill(6) + '_org.png'
        urllib.request.urlretrieve(image_url, image_name)

        wine_image_list.append(wine_num+'_org.png')

        num += 1

# 워크북(엑셀파일)을 새로 만듭니다.
wb = openpyxl.Workbook()

# 현재 활성화된 시트를 선택합니다.
sheet = wb.active
# A1셀에 hello world!를 입력합니다.
for index in range(len(wine_no)) : 
    i = index + 1
    sheet.cell(row = i, column = 1).value = wine_no[index]
    sheet.cell(row = i, column = 2).value = wine_en_name[index]
    sheet.cell(row = i, column = 3).value = wine_kor_name[index]
    sheet.cell(row = i, column = 4).value = wine_type[index]
    sheet.cell(row = i, column = 5).value = wine_winery[index]
    sheet.cell(row = i, column = 6).value = wine_winery_en[index]

    sheet.cell(row = i, column = 7).value = wine_country[index]
    sheet.cell(row = i, column = 8).value = wine_region[index]
    sheet.cell(row = i, column = 9).value = wine_grape[index]
    sheet.cell(row = i, column = 10).value = wine_size[index]
    sheet.cell(row = i, column = 11).value = wine_temp[index]

    sheet.cell(row = i, column = 12).value = wine_image_list[index]

    # sheet.cell(row = i, column = 9).value = wine_win[index]
    sheet.cell(row = i, column = 15).value = wine_desc[index]
    sheet.cell(row = i, column = 16).value = winery_desc[index]
    # sheet.cell(row = i, column = 12).value = wine_sweetness[index]

wb.save('mervin.xlsx')



