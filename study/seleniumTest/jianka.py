# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Jianka(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://fyonecardpre.cdwit120.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_jianka(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//div[@id='app']/div/div[6]/div[2]/div/div/div/div").click()
        driver.find_element_by_css_selector("div.new").click()
        driver.find_element_by_css_selector("input.fy-flex-2").clear()
        driver.find_element_by_css_selector("input.fy-flex-2").send_keys("10000000072")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("111111")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/button").click()
        driver.find_element_by_css_selector("div.select.correct").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]").click()
        driver.find_element_by_css_selector("div.picker-item.picker-selected").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_id("card_no").clear()
        driver.find_element_by_id("card_no").send_keys("990900012195772")
        driver.find_element_by_id("idcard").clear()
        driver.find_element_by_id("idcard").send_keys("510107201503310045")
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"许青未")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/button").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/article/div/div[3]/div[3]/img").click()
        driver.find_element_by_css_selector("li.mint-actionsheet-listitem").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_css_selector("input.text").clear()
        driver.find_element_by_css_selector("input.text").send_keys("166")
        driver.find_element_by_xpath("(//input[@type='number'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='number'])[3]").send_keys("66")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"四川省成都市武侯区跳伞塔街道跳伞塔街道")
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys(u"四川省成都市武侯区跳伞塔街道跳伞塔街道")
        driver.find_element_by_xpath("(//input[@type='text'])[10]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[11]").click()
        driver.find_element_by_css_selector("span.mint-datetime-action.mint-datetime-confirm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/article[2]/div/div[3]/div/div").click()
        driver.find_element_by_css_selector("li.mint-actionsheet-listitem").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/article[2]/div/div[4]/div/div[2]").click()
        driver.find_element_by_css_selector("li.mint-actionsheet-listitem").click()
        driver.find_element_by_xpath("(//input[@type='text'])[13]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='number'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("5")
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/article[2]/div/div[8]/div[2]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='number'])[6]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='number'])[7]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='number'])[8]").click()
        driver.find_element_by_css_selector("div.confirm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").send_keys(u"测试")
        driver.find_element_by_xpath("(//input[@type='text'])[20]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").send_keys("510107201503310045")
        driver.find_element_by_xpath("(//input[@type='number'])[10]").clear()
        driver.find_element_by_xpath("(//input[@type='number'])[10]").send_keys("10000000072")
        driver.find_element_by_xpath("(//input[@type='text'])[22]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[22]").send_keys(u"详细的数据详细的数据详细的数据")
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/button").click()
        driver.find_element_by_css_selector("input.text").clear()
        driver.find_element_by_css_selector("input.text").send_keys("66")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").click()
        driver.find_element_by_css_selector("div.cancel").click()
        driver.find_element_by_xpath("(//input[@type='number'])[3]").click()
        driver.find_element_by_css_selector("div.cancel").click()
        driver.find_element_by_xpath("(//input[@type='number'])[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]").click()
        driver.find_element_by_css_selector("div.picker-item.picker-selected").click()
        driver.find_element_by_css_selector("div.cancel").click()
        driver.find_element_by_css_selector("input[type=\"text\"]").click()
        driver.find_element_by_xpath("//div[@id='datetime']/div/div[2]/div/div/div[20]").click()
        driver.find_element_by_css_selector("span.mint-datetime-action.mint-datetime-confirm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_css_selector("div.cancel").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/button").click()
        driver.find_element_by_css_selector("div.confirm.flex-grow-a").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
