# coding = utf-8
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()       #将浏览器最大化

driver.get('https://fyonecardpre.cdwit120.com/newuser')
builder = ActionChains(driver)
builder.key_down(Keys.F12).perform()
print(driver.title)
time.sleep(3)  # 休眠3秒
driver.quit()

