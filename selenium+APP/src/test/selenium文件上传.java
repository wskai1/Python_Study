package test;

import com.google.common.base.Verify;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;

import java.io.File;

public class selenium文件上传 {
    public static void main(String[] args) throws Exception {
        WebDriver driver = new ChromeDriver();
        // 获取当前页面句柄
        String handle = driver.getWindowHandle();
        // 获取所有页面的句柄，并循环判断不是当前的句柄
        for (String handles : driver.getWindowHandles()) {
            if (!handles.equals(handle))
                continue;
            driver.switchTo().window(handles);
        }
        driver.get("https://www.baidu.cn");
        driver.manage().window().maximize();

       driver.findElement(By.xpath("//*[@id=\"form\"]/span[1]/span")).click();
        //定位上传按钮， 添加本地文件
        driver.findElement(By.xpath("//*[@id=\"form\"]/div/div[2]/div[2]/input")).sendKeys("C:\\Users\\wsk\\Desktop\\a.jpg");
        Thread.sleep(5000);
    }
}
