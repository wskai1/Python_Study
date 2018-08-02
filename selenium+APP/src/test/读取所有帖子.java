package test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;

import java.util.List;
import java.util.concurrent.TimeUnit;

import static org.junit.Assert.fail;

public class 读取所有帖子 {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new ChromeDriver();
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testWei() throws Exception {
    // 获取当前页面句柄
    String handle = driver.getWindowHandle();
    // 获取所有页面的句柄，并循环判断不是当前的句柄
    for (String handles : driver.getWindowHandles()) {
      if (!handles.equals(handle))
        continue;
      driver.switchTo().window(handles);
    }
    driver.get("http://116.62.52.165:30080/pregnantbaby");
    Thread.sleep(1000);
    for (int i=0;i<15;i++){
//      driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[3]/div[1]/a[1]")).sendKeys(Keys.DOWN);
      ((JavascriptExecutor)driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
      Thread.sleep(300);
      System.out.println(i);
    }
    Thread.sleep(2000);
    List<WebElement> li = driver.findElements(By.tagName("li"));
   for(int i=0;i<li.size();i++){
     li.get(i).click();
     Thread.sleep(200);
     ((JavascriptExecutor)driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
     driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]")).click();
     li = driver.findElements(By.tagName("li"));
     System.out.println(i);
   }
    ((JavascriptExecutor)driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
    Thread.sleep(2000);
    ((JavascriptExecutor)driver).executeScript("scrollTo(0, 0)");
    Thread.sleep(2000);
    ((JavascriptExecutor)driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
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
