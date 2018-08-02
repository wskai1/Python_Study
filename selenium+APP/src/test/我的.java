package test;

import java.util.List;
import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;

import org.junit.*;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class 我的 {
    private WebDriver driver;
    private String baseUrl;
    private boolean acceptNextAlert = true;
    private StringBuffer verificationErrors = new StringBuffer();

    @Before
    public void setUp() throws Exception {
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void test() throws Exception {
        // 获取当前页面句柄
        String handle = driver.getWindowHandle();
        // 获取所有页面的句柄，并循环判断不是当前的句柄
        for (String handles : driver.getWindowHandles()) {
            if (!handles.equals(handle))
                continue;
            driver.switchTo().window(handles);
        }
        driver.get("https://fyonecardpre.cdwit120.com?redirect=mine");
        Thread.sleep(1000);
        driver.findElement(By.cssSelector("input.fy-flex-2")).clear();
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
        Thread.sleep(1000);
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/section/a/div")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/a[2]")).click();
        for (int i = 0; i < 10; i++) {
            ((JavascriptExecutor) driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
            Thread.sleep(500);
        }
        List<WebElement> elements = driver.findElements(By.xpath("//div[@slot='loadMorePage']"));
        System.out.println(elements.size());
        for (int i = 0; i < elements.size(); i++) {
            elements.get(i).click();
            driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]/p[2]")).click();
            elements = driver.findElements(By.xpath("//div[@slot='loadMorePage']"));
            System.out.println(i);
        }
        driver.findElement(By.linkText("点赞")).click();
        Thread.sleep(500);
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div/div/div[2]/div[3]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]/p[2]")).click();
        driver.findElement(By.linkText("评论")).click();

        //个人健康档案

        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div[2]/div/div[3]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/footer/a[4]")).click();
        driver.findElement(By.cssSelector("img[alt=\"宝宝健康档案\"]")).click();
        driver.findElement(By.cssSelector("div.text")).click();
        //我的一卡通
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[1]/div[1]/div[3]/img")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div[1]")).click();
        List<WebElement> calendars = driver.findElements(By.xpath("//div[@slot='loadMorePage']"));
        System.out.println(calendars.size());
        for (int i = 0; i < calendars.size(); i++) {
            calendars.get(i).click();
            driver.findElement(By.className("left")).click();
            calendars = driver.findElements(By.className("calendar"));
        }
        driver.findElement(By.xpath("//div/div/div/div[1]")).click();//返回
        Thread.sleep(2000);
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[3]/div/div[2]/div[2]")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div[3]/div/div[3]/div[2]")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div[3]/div/div[4]/div[2]")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div/div/div[2]/div[2]")).click();

        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[1]/div[3]/div[2]")).click();
        driver.findElement(By.xpath("/html/body/div/div/header/div[3]/div/p[1]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[1]/a[1]")).click();
        driver.findElement(By.linkText("评论")).click();
        Thread.sleep(1000);
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div/div[3]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/header/div[1]")).click();
        driver.findElement(By.linkText("点赞")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.cssSelector("pre")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div/div[5]/div")).click();
        driver.findElement(By.name("comment")).clear();
        driver.findElement(By.name("comment")).sendKeys("6");
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[2]")).click();
        driver.findElement(By.name("comment")).clear();
        driver.findElement(By.name("comment")).sendKeys("!@#$%^&*\n        dsad \n            dsada");
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/article/div[1]/p")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div/article/div/div")).click();
        driver.findElement(By.cssSelector("div.right_title")).click();
        driver.findElement(By.cssSelector("div.share-item.share-friends")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.cssSelector("pre")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.xpath("//div[@id='mine-pregnant-baby']/header/div")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div/div/div[4]/div[2]")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div/div/div[4]/div[2]")).click();
        driver.findElement(By.linkText("已收藏")).click();
        driver.findElement(By.linkText("已报名")).click();

        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/ul/div/div/div/li[2]/div/div[1]/div[1]")).click();
        driver.findElement(By.xpath("//div[@id='videoBox']/div")).click();
        driver.findElement(By.xpath("//div[@id='app']/div/div/header/div")).click();
        driver.findElement(By.linkText("已收藏")).click();
        driver.findElement(By.linkText("已报名")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/ul/div/div/div/li[2]/div/div[1]")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.cssSelector("p.text")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]/p[2]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[1]/div[5]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div/div/li/div")).click();
        //资讯详情 滚动条下拉
        for (int i = 0; i < 5; i++) {
//      driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[3]/div[1]/a[1]")).sendKeys(Keys.DOWN);
            ((JavascriptExecutor) driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
            Thread.sleep(300);
            System.out.println(i);
        }
        ((JavascriptExecutor) driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
        ((JavascriptExecutor) driver).executeScript("scrollTo(0, 0)");
        ((JavascriptExecutor) driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[3]/div/img")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[3]/div/img")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
//系统设置
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[1]")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div/div[1]/div")).click();
        driver.findElement(By.xpath("//*[@id=\"app\"]/div/header/div[1]")).click();
        driver.findElement(By.cssSelector("div.log-out")).click();
        driver.findElement(By.cssSelector("input.fy-flex-2")).clear();
        driver.findElement(By.cssSelector("input.fy-flex-2")).sendKeys("13333333333");
        driver.findElement(By.xpath("//input[@type='password']")).clear();
        driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
        driver.findElement(By.xpath("//div[@id='app']/div/div[2]/button")).click();
        driver.findElement(By.linkText("我的")).click();

        //意见反馈
//        driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[2]/div[2]")).click();

//        driver.findElement(By.id("post_content")).clear();
//        driver.findElement(By.id("post_content")).sendKeys("@#$意见");
//        driver.findElement(By.id("html5_1c55ia1066j8b081vkqm9p1sub4")).clear();
//        driver.findElement(By.id("html5_1c55ia1066j8b081vkqm9p1sub4")).sendKeys("");
//        driver.findElement(By.id("fileSubmit")).click();
//        driver.findElement(By.cssSelector("a.banner-img-box > img.img")).click();
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
