package test;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class wei {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new ChromeDriver();
    baseUrl = "http://116.62.52.165:30080";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testWei() throws Exception {
    driver.get(baseUrl + "/newuser");
    driver.findElement(By.cssSelector("div.link")).click();
    driver.findElement(By.cssSelector("div.left_title")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
    driver.findElement(By.cssSelector("input.flex-grow-a")).click();
    driver.findElement(By.cssSelector("input.link")).clear();
    driver.findElement(By.cssSelector("input.link")).sendKeys("1");
    driver.findElement(By.xpath("//div[@id='app']/div/header/div[3]/div")).click();
    driver.findElement(By.linkText("资讯")).click();
    driver.findElement(By.linkText("帖子")).click();
    ((JavascriptExecutor) driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div/li[29]/div/div/div[2]/span")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("p.icon")).click();
    driver.findElement(By.cssSelector("div.right_title")).click();
    driver.findElement(By.cssSelector("p.icon")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[3]/div/div[2]/div/div[2]")).click();
    driver.findElement(By.cssSelector("p.icon")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[4]/div/div")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div")).click();
    driver.findElement(By.cssSelector("div.new")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div")).click();
    driver.findElement(By.cssSelector("div.archives.flex-grow-a")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div")).click();
    driver.findElement(By.cssSelector("div.process.flex-grow-a")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div")).click();
    driver.findElement(By.linkText("*查看《一卡通建卡流程》")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div[2]")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div[3]")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div[2]/div[4]")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div/div")).click();
    driver.findElement(By.linkText("产妇建卡")).click();
    driver.findElement(By.cssSelector("div.new")).click();
    driver.findElement(By.cssSelector("p.icon")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("产妇建卡")).click();
    driver.findElement(By.cssSelector("div.archives.flex-grow-a")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("产妇建卡")).click();
    driver.findElement(By.cssSelector("div.process.flex-grow-a")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("产妇建卡")).click();
    driver.findElement(By.linkText("*查看《一卡通建卡流程》")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.linkText("健康档案")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("产检预约")).click();
    driver.findElement(By.linkText("产检报告")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("儿保建档")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    Thread.sleep(3000);
    driver.findElement(By.xpath("//body/div[2]")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("儿保日历")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[5]/div/div")).click();
    driver.findElement(By.linkText("儿保预约")).click();
    driver.findElement(By.linkText("儿童健康")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("img.img")).click();
    driver.findElement(By.cssSelector("div.content-title")).click();
    driver.findElement(By.cssSelector("img.header-right-img")).click();

    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("img.img")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li[2]/div/div/div")).click();
    driver.findElement(By.cssSelector("img.header-right-img")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("img.img")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li[6]/div/div/div")).click();
    driver.findElement(By.cssSelector("img.header-right-img")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[7]/div/div")).click();
    driver.findElement(By.cssSelector("div.nav-item.fy-flex-2 > div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/nav/div[3]/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/nav/div[4]/div")).click();
    driver.findElement(By.cssSelector("img[alt=\"热门资讯\"]")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("img[alt=\"精品课程\"]")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li/div/div/div[2]")).click();
    driver.findElement(By.cssSelector("img.collection-icon")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.content-title")).click();
    driver.findElement(By.cssSelector("img.collection-icon")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.left.fy-flex-2")).click();
    driver.findElement(By.cssSelector("button.btn.btn-label")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
    driver.findElement(By.cssSelector("div.microclass-icon.icon-img")).click();
    driver.findElement(By.cssSelector("div.nav-item.fy-flex-2 > div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/nav/div[3]/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/nav/div[4]/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/nav/div[3]/div")).click();
    driver.findElement(By.cssSelector("div.nav-item.fy-flex-2 > div")).click();
    driver.findElement(By.cssSelector("div.nav-item.fy-flex-1 > div")).click();
    driver.findElement(By.cssSelector("div.content-title")).click();
    driver.findElement(By.linkText("2")).click();
    driver.findElement(By.cssSelector("button.btn.btn-label")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.microclass-icon.icon-img")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/ul/div/div/div/li[4]/div/div/div")).click();
    driver.findElement(By.linkText("2")).click();
    driver.findElement(By.cssSelector("span.collection-text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/footer/a[2]/div[2]")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/ul/div/div/div/li[3]/div/div/div")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.nav-item.fy-flex-2 > div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/ul/div/div/div/li/div/div/div[2]")).click();
    driver.findElement(By.cssSelector("span.collection-text")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.microclass-icon.icon-img")).click();
    driver.findElement(By.cssSelector("div.pregnantbaby-icon.icon-img")).click();
    driver.findElement(By.cssSelector("img.img")).click();
    driver.findElement(By.cssSelector("img.img")).click();
    driver.findElement(By.linkText("#宝宝健康#")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.linkText("#宝宝#")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.linkText("#标签#")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li[10]/div/div[2]/p/pre")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div/header/div")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
    driver.findElement(By.linkText("更多标签")).click();
    driver.findElement(By.cssSelector("div.topic-desc")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li[23]/div/div[2]/p")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li[2]/div[2]")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.circle-tag > a > img")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/li[5]/div")).click();
    driver.findElement(By.cssSelector("pre")).click();
    driver.findElement(By.cssSelector("span.right-label.no-follow")).click();
    driver.findElement(By.cssSelector("p.icon")).click();
    driver.findElement(By.xpath("//div[@id='app']/div/footer/a[3]/div[2]")).click();
    driver.findElement(By.linkText("关注")).click();
    driver.findElement(By.cssSelector("p.text")).click();
    driver.findElement(By.cssSelector("div.mine-icon.icon-img")).click();
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
