
# coding = utf-8
import string

from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

browser = webdriver.Chrome(chrome_options=options)

browser.get("http://item.jd.com/7081550.html")
s=browser.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[1]').text
p=browser.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]').text
print(s)
print(p)

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