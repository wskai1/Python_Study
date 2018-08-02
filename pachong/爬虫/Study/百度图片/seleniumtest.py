# coding = utf-8
import string

import time

import requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# 获取页面的URL
driver.get("http://image.baidu.com/")
driver.find_element_by_xpath('//*[@id="wrapper_head_box"]/div/div/div/div/div[3]/a[1]').click()
for i in range(10):
    js="var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(1)
for index,i in enumerate(driver.find_elements_by_tag_name("li")):
    try:
        pic = requests.get(i.get_attribute('data-objurl'))
        string = 'E:/wsk/Python/pachong/爬虫/Study/百度图片/图片/' + str(index) + '.jpg'
        with open(string, 'wb') as f:
            f.write(pic.content)
            print('成功下载')
    except Exception as e:
        print('下载图片失败:')
        print(e)
        continue
driver.close()
driver.quit()