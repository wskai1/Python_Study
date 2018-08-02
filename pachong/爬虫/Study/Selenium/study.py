import time

from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get("http://www.baidu.com")
# time.sleep(5)
# print(browser.page_source)
# browser.close()
# browser.quit()
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
input_first = browser.find_element_by_id("J_SiteNavLogin")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first.text)
print(input_second.text)
print(input_third.text)
browser.close()
browser.quit()

# 返回  前进
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
browser.quit()


browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())


browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

