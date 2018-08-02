# -*- coding:utf-8 -*-  

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

mobile_emulation = {"deviceName": "iPhone 7"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://fyonecardpre.cdwit120.com?redirect=mine")
driver.find_element_by_class_name('link').click()
driver.find_element_by_xpath('//*[@id="app"]/div/footer/a[1]/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/footer/a[2]/div[1]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/footer/a[3]/div[1]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/footer/a[4]/div[1]/div').click()
time.sleep(2)

driver.find_element(By.CLASS_NAME("input.fy-flex-2")).clear();
driver.findElement(By.cssSelector("input.fy-flex-2")).sendKeys("13333333338");
driver.findElement(By.xpath("//input[@type='password']")).clear();
driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
driver.findElement(By.xpath("//div[@id='app']/div/div[2]/button")).click();
driver.findElement(By.cssSelector("div.header-content")).click();
driver.findElement(By.linkText("退出登录")).click();
driver.findElement(By.cssSelector("input.fy-flex-2")).clear();
driver.findElement(By.cssSelector("input.fy-flex-2")).sendKeys("13333333338");
driver.findElement(By.xpath("//input[@type='password']")).clear();
driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
driver.findElement(By.xpath("//div[@id='app']/div/div[2]/button")).click();
driver.findElement(By.cssSelector("div.link")).click();
driver.findElement(By.cssSelector("div.mine-icon.icon-img")).click();
driver.findElement(By.cssSelector("img.img")).click();
driver.findElement(By.linkText("退出登录")).click();
driver.findElement(By.cssSelector("input.fy-flex-2")).clear();
driver.findElement(By.cssSelector("input.fy-flex-2")).sendKeys("13333333338");
driver.findElement(By.xpath("//input[@type='password']")).clear();
driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
driver.findElement(By.xpath("//div[@id='app']/div/div[2]/button")).click();
driver.findElement(By.linkText("我的")).click();
driver.findElement(By.cssSelector("div.header-content")).click();
driver.findElement(By.xpath("//*[@id=\"user_nick\"]")).clear();
driver.findElement(By.xpath("//*[@id=\"user_nick\"]")).sendKeys("");
driver.findElement(By.id("user_nick")).clear();
driver.findElement(By.id("user_nick")).sendKeys("");
driver.findElement(By.cssSelector("p.text")).click();
driver.findElement(By.cssSelector("img.img")).click();
driver.findElement(By.id("user_nick")).clear();
driver.findElement(By.id("user_nick")).sendKeys("");
driver.findElement(By.id("fileSubmit")).click();
driver.findElement(By.id("user_nick")).clear();
driver.findElement(By.id("user_nick")).sendKeys("www");
driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[3]")).click();
driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]/p[2]")).click();
time.sleep(1000);
driver.findElement(By.xpath("//*[@id=\"app\"]/div/section/a/div")).click();
driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/a[2]")).click();
# for i in range(10):
#     ((JavascriptExecutor)driver).executeScript("window.scrollTo(0,document.body.scrollHeight)");
# time.sleep(500);
# List<WebElement>elements=driver.findElements(By.xpath("//div[@slot='loadMorePage']"));
# System.out.println(elements.size());
# for(inti=0;i<elements.size();i++){
# elements.get(i).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]/p[2]")).click();
# elements=driver.findElements(By.xpath("//div[@slot='loadMorePage']"));
# System.out.println(i);
# }
# driver.findElement(By.linkText("点赞")).click();
# Thread.sleep(500);
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div/div/div[2]/div[3]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]/p[2]")).click();
# driver.findElement(By.linkText("评论")).click();
#
# //个人健康档案
#
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div[2]/div/div[3]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/footer/a[4]")).click();
# driver.findElement(By.cssSelector("img[alt=\"宝宝健康档案\"]")).click();
# driver.findElement(By.cssSelector("div.text")).click();
# //我的一卡通
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[1]/div[1]/div[3]/img")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div[1]")).click();
# List<WebElement>calendars=driver.findElements(By.xpath("//div[@slot='loadMorePage']"));
# System.out.println(calendars.size());
# for(inti=0;i<calendars.size();i++){
# calendars.get(i).click();
# driver.findElement(By.className("left")).click();
# calendars=driver.findElements(By.className("calendar"));
# }
# driver.findElement(By.xpath("//div/div/div/div[1]")).click();//返回
# Thread.sleep(2000);
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div[2]/div[2]")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div[3]/div/div[3]/div[2]")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div[3]/div/div[4]/div[2]")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div/div/div[2]/div[2]")).click();
#
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[1]/div[3]/div[2]")).click();
# driver.findElement(By.xpath("/html/body/div/div/header/div[3]/div/p[1]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[1]/a[1]")).click();
# driver.findElement(By.linkText("评论")).click();
# Thread.sleep(1000);
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div/div[3]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]")).click();
# driver.findElement(By.linkText("点赞")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.cssSelector("pre")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div/div[5]/div")).click();
# driver.findElement(By.name("comment")).clear();
# driver.findElement(By.name("comment")).sendKeys("6");
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[2]")).click();
# driver.findElement(By.name("comment")).clear();
# driver.findElement(By.name("comment")).sendKeys("!@#$%^&*\ndsad\ndsada");
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/article/div[1]/p")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div/article/div/div")).click();
# driver.findElement(By.cssSelector("div.right_title")).click();
# driver.findElement(By.cssSelector("div.share-item.share-friends")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.cssSelector("pre")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.xpath("//div[@id='mine-pregnant-baby']/header/div")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div/div/div[4]/div[2]")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div/div/div[4]/div[2]")).click();
# driver.findElement(By.linkText("已收藏")).click();
# driver.findElement(By.linkText("已报名")).click();
#
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/ul/div/div/div/li[2]/div/div[1]/div[1]")).click();
# driver.findElement(By.xpath("//div[@id='videoBox']/div")).click();
# driver.findElement(By.xpath("//div[@id='app']/div/div/header/div")).click();
# driver.findElement(By.linkText("已收藏")).click();
# driver.findElement(By.linkText("已报名")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/ul/div/div/div/li[2]/div/div[1]")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.cssSelector("p.text")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]/p[2]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[1]/div[5]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div/div/li/div")).click();
# //资讯详情滚动条下拉
# for(inti=0;i<5;i++){
# //driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[3]/div[1]/a[1]")).sendKeys(Keys.DOWN);
# ((JavascriptExecutor)driver).executeScript("window.scrollTo(0,document.body.scrollHeight)");
# Thread.sleep(300);
# System.out.println(i);
# }
# ((JavascriptExecutor)driver).executeScript("window.scrollTo(0,document.body.scrollHeight)");
# ((JavascriptExecutor)driver).executeScript("scrollTo(0,0)");
# ((JavascriptExecutor)driver).executeScript("window.scrollTo(0,document.body.scrollHeight)");
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[3]/div/img")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[3]/div/img")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
# //系统设置
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[1]")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div/div[1]/div")).click();
# driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
# driver.findElement(By.cssSelector("div.log-out")).click();
# driver.findElement(By.cssSelector("input.fy-flex-2")).clear();
# driver.findElement(By.cssSelector("input.fy-flex-2")).sendKeys("13333333333");
# driver.findElement(By.xpath("//input[@type='password']")).clear();
# driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
# driver.findElement(By.xpath("//div[@id='app']/div/div[2]/button")).click();
# driver.findElement(By.linkText("我的")).click();
time.sleep(5)
driver.quit()