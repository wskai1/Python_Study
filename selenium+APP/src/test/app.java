package test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.NoAlertPresentException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeUnit;
import static org.testng.Assert.fail;
public class app {
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
            driver.findElement(By.className("link")).click();
            Thread.sleep(3000);
            driver.findElement(By.cssSelector("div.microclass-icon.icon-img")).click();
            Thread.sleep(3000);
            driver.findElement(By.cssSelector("div.pregnantbaby-icon.icon-img")).click();
            driver.findElement(By.linkText("首页")).click();
            driver.findElement(By.cssSelector("div.mine-icon.icon-img")).click();
            driver.findElement(By.cssSelector("input.fy-flex-2")).clear();
            driver.findElement(By.cssSelector("input.fy-flex-2")).sendKeys("13350700581");
            driver.findElement(By.xpath("//input[@type='password']")).clear();
            driver.findElement(By.xpath("//input[@type='password']")).sendKeys("111111");
            driver.findElement(By.xpath("//div[@id='app']/div/div[2]/button")).click();
            driver.findElement(By.linkText("孕婴圈")).click();
            driver.findElement(By.cssSelector("div.microclass-icon.icon-img")).click();
            driver.findElement(By.cssSelector("div.home-icon.icon-img")).click();
            driver.findElement(By.cssSelector("div.left_title")).click();
            driver.findElement(By.xpath("//header[@id='header']/div[2]/div/div/div")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/div[2]/ul[2]/li")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
            driver.findElement(By.cssSelector("div.home-icon.icon-img")).click();
            driver.findElement(By.cssSelector("div.left_title")).click();
            driver.findElement(By.cssSelector("p.title")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/div[3]/div/div[2]/div[2]")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/div[5]/div/div[2]/div/p")).click();
            driver.findElement(By.cssSelector("p.text")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/div[2]/div/div/div[10]/div/div[2]/div[2]")).click();
            driver.findElement(By.xpath("//div[@id='app']/div/header/div")).click();
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


