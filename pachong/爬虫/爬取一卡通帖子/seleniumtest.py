# coding = utf-8
import string

import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()


# 获取页面的URL
driver.get("https://fyonecardpre.cdwit120.com")
driver.find_element_by_class_name("link").click()
time.sleep(1)
s=driver.find_element_by_xpath("//*[@id='app']/div/footer/a[4]")
print(s.text)
s.click()
driver.find_element_by_css_selector("input.fy-flex-2").clear()
driver.find_element_by_css_selector("input.fy-flex-2").send_keys("10000000072")
driver.find_element_by_xpath("//input[@type='password']").clear()
driver.find_element_by_xpath("//input[@type='password']").send_keys("111111")
driver.find_element_by_xpath("//div[@id='app']/div/div[2]/button").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div/footer/a[3]").click()
time.sleep(5)

#将滚动条移动到页面的底部
for i in range(20):
    js="var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(3)
    print(i)
f = open("tiezi.txt", "w+",encoding='utf-8')
for link in driver.find_elements_by_tag_name("li"):
    username=link.find_element_by_class_name("user-name").text
    time=link.find_element_by_class_name("grey-label").text
    detail=link.find_element_by_class_name("detail-info").text
    f.write('作者:'+username+'\n')
    f.write('时间:'+time+'\n')
    f.write('帖子内容：'+detail+'\n')
    f.write('\n')
f.close()
driver.close()
driver.quit()