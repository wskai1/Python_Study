package test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.List;

public class test {
    public static void main(String[] args) throws InterruptedException {
        //引入geckodriver驱动  ---第二个参数是驱动所在路径
        System.setProperty("webdriver.chrome.marionette", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");
        //新建一个firefox浏览器实例
        ChromeOptions options = new ChromeOptions();
        //通过配置参数禁止data;的出现
        options.addArguments("--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Default");
        //通过配置参数删除“您使用的是不受支持的命令行标记：--ignore-certificate-errors。稳定性和安全性会有所下降。”提示
        options.addArguments("--start-maximized",
                "allow-running-insecure-content", "--test-type");
        WebDriver driver = new ChromeDriver();
        WebDriver newWindow=null;
        Thread.sleep(2000);
        driver.manage().window().maximize();//浏览器最大化
        //打开百度首页
        driver.get("http://www.baidu.com");
        //获取当前页面句柄
        String current_handle = driver.getWindowHandle();
        //根据id获取输入框
        WebElement textInput = driver.findElement(By.id("kw"));
        //在输入框输入“Selenium”
        textInput.sendKeys("Selenium");
        //根据id获取“百度一下”按钮
        WebElement submit = driver.findElement(By.id("su"));
        //点击按钮
        submit.click();
        Thread.sleep(1000);
        List<WebElement> list = driver.findElements(By.xpath("//a"));
        for (int i=0;i<list.size();i++){
            System.out.println(list.get(i).getText()+list.get(i).getAttribute("href"));
        }
        List<WebElement> list1 = driver.findElements(By.xpath("//a"));

//退出所有的浏览器
        driver.switchTo().window(current_handle);
        driver.quit();
    }
}