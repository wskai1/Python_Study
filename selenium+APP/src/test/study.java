package test;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeUnit;

import static org.testng.Assert.fail;

public class study {
    private WebDriver driver;
    private String baseUrl;
    private boolean acceptNextAlert = true;
    private StringBuffer verificationErrors = new StringBuffer();

    @BeforeClass(alwaysRun = true)
    public void setUp() throws Exception {
        driver = new ChromeDriver();
        baseUrl = "http://116.62.52.165:30080";
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        driver.manage().window().maximize();//浏览器最大化

    }

    @Test
    public void testA() throws Exception {
        driver.get(baseUrl + "/");
        WebElement app = driver.findElement(By.id("app"));
        String text = app.getText();
        System.out.println(text);
        WebElement element = driver.findElement(By.xpath("//*"));
        System.out.println(element.getText());
        WebElement title = driver.findElement(By.className("title"));
        System.out.println(title.getText() + "" + title.getTagName() + title.getSize());
        WebElement element1 = driver.findElement(By.xpath("//div[@class='title']"));
        System.out.println(element1.getText() + "" + element1.getTagName() + element1.getSize());
        List<WebElement> elements = driver.findElements(By.xpath("//div[@id='app']/*/*/div[1]"));
        System.out.println(elements.get(1).getText() + "========");

        WebElement top = driver.findElement(By.className("link"));
        top.click();
        driver.findElement(By.className("left_title")).click();
        // driver.findElement(By.xpath("//input[@class='fy-flex-2']")).clear();
        // driver.findElement(By.xpath("//input[@class='fy-flex-2']")).sendKeys("13350700581");
        List<WebElement> list = driver.findElements(By.xpath("//input[@class='fy-flex-2']"));
        list.get(0).sendKeys("13350700581");
        list.get(1).sendKeys("111111");
//        System.out.println(list.size());

        String a = driver.findElement(By.tagName("button")).getAttribute("disabled");
        System.out.println(a + "---");
        if (a != null) {
            System.out.println("button不可点击");
        }
        System.out.println(list.get(1).getText());
        list.get(0).clear();
        driver.findElement(By.xpath("//input[@type='password']")).clear();
        driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
        list.get(0).sendKeys("13333333333");
        driver.findElement(By.tagName("button")).click();
        driver.findElement(By.xpath("//header[@id='header']/div[2]/div/div/div")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div[2]/ul[2]/li")).click();
        List<WebElement> calendars = driver.findElements(By.className("calendar"));
        System.out.println(calendars.size());
        for (int i=0;i<calendars.size();i++) {
           calendars.get(i).click();
            driver.findElement(By.className("left")).click();
          calendars = driver.findElements(By.className("calendar"));
        }
        driver.findElement(By.className("left")).click();
        driver.findElement(By.xpath("//input[@type='text']")).click();
        //driver.findElement(By.cssSelector("input.link")).sendKeys("聪明的宝宝");
        driver.findElement(By.xpath("//input[@class='link']")).sendKeys("聪明的宝宝");
        driver.findElement(By.xpath("//div[@slot]")).click();
        List<WebElement> as = driver.findElements(By.tagName("a"));
        for (WebElement ass:as
             ) {
            ass.click();
        }
      driver.findElement(By.tagName("p")).click();
        List<WebElement> elements1 = driver.findElements(By.cssSelector("div.flex-grow-a"));
        for (int i=0;i<elements1.size();i++){
            elements1.get(i).click();
            Thread.sleep(1000);
            List<WebElement> as1 = driver.findElements(By.tagName("a"));
            for (WebElement ass:as1
                    ) {
                ass.click();
            }driver.findElement(By.tagName("p")).click();
            elements1 = driver.findElements(By.cssSelector("div.flex-grow-a"));
        }
        driver.findElement(By.className("icon")).click();
      //  driver.findElement(By.className("left")).click();//取消上面的注释就需要注释掉改行
        Thread.sleep(1000);
        String s = driver.findElement(By.cssSelector("div.right-box")).getText();
        System.out.println(s);
        driver.findElement(By.className("changeLink")).click();
        List<WebElement> list1 = driver.findElements(By.xpath("//div[@id='app']/div/div[3]/div/div[2]/div//div"));
        System.out.println(list1.size()+"====="+list1.get(2).getText());
        driver.findElement(By.xpath("//div[@id='app']/div/div[3]/div/div[2]/div/div[5]")).click();
//        for (int i=0;i<list1.size();i++){
//            list1.get(i).click();
//            Thread.sleep(2000);
//            driver.findElement(By.className("changeLink")).click();
////            if (i!=0){
////                System.out.println(driver.findElement(By.cssSelector("div.info")).getText());
////            }
//            list1 = driver.findElements(By.xpath("//div[@id='app']/div/div[3]/div/div[2]/div/div"));
//        }
        Thread.sleep(30000);

//        driver.findElement(By.className("fy-flex-justify-center")).click();
//        List<WebElement> lis = driver.findElements(By.xpath("//li"));
//        System.out.println(lis.size());
//        Thread.sleep(20000);

    }

    @AfterClass(alwaysRun = true)
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


