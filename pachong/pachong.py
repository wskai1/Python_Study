
# coding = utf-8
import string

from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

browser = webdriver.Chrome(chrome_options=options)

browser.get("https://www.baidu.com/")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
print(browser.title)  # 把页面title 打印出来

# 获取页面的URL
browser.get("https://hao.360.cn/")
f = open("seleniumTest.txt", "w+",encoding='utf-8')
for link in browser.find_elements_by_tag_name("a"):
    # print(link.get_attribute('text'),link.get_attribute("href"))
    a = str(link.get_attribute('href'))
    b = str(link.get_attribute("text"))
    f.write(b+"--")
    f.write(a)
    f.write('\n')
f.close()
browser.close()
browser.quit()
