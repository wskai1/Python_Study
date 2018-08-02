package test;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class selenium {
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
        driver.get("https://m.baidu.cn");
        driver.manage().window().setSize(new Dimension(480, 800));
        driver.manage().window().maximize();
        //get 到百度首页
        driver.get("https://www.baidu.com/");
        System.out.printf("now accesss %s \n", driver.getCurrentUrl());

        //点击“新闻” 链接
        driver.findElement(By.linkText("新闻")).click();
        System.out.printf("now accesss %s \n", driver.getCurrentUrl());
        //刷新页面
        driver.navigate().refresh();

        //执行浏览器后退
        driver.navigate().back();
        System.out.printf("back to %s \n", driver.getCurrentUrl());

        //执行浏览器前面        driver.navigate().forward();
        System.out.printf("forward to %s \n", driver.getCurrentUrl());

        //鼠标
        driver.get("https://www.baidu.com/");
        //鼠标悬停
        WebElement search_setting = driver.findElement(By.linkText("设置"));
        Actions action = new Actions(driver);
        action.clickAndHold(search_setting).perform();
        String s = driver.findElement(By.xpath("//*[@id=\"wrapper\"]/div[6]/a[4]")).getText();
        System.out.println(s);
//        // 鼠标右键点击指定的元素
//        action.contextClick(driver.findElement(By.id("element"))).perform();
//        // 鼠标右键点击指定的元素
//
//        action.doubleClick(driver.findElement(By.id("element"))).perform();
//        // 鼠标拖拽动作， 将 source 元素拖放到 target 元素的位置。
//        WebElement source = driver.findElement(By.name("element"));
//        WebElement target = driver.findElement(By.name("element"));
//        action.dragAndDrop(source, target).perform();
        // 释放鼠标
        driver.get("https://www.baidu.com");
        WebElement input = driver.findElement(By.id("kw"));
        //输入框输入内容
        input.sendKeys("seleniumm");
        Thread.sleep(2000);
        //删除多输入的一个 m
        input.sendKeys(Keys.BACK_SPACE);
        Thread.sleep(2000);
        //输入空格键+“教程”
        input.sendKeys(Keys.SPACE);
        input.sendKeys("教程");
        Thread.sleep(2000);

       //ctrl+a 全选输入框内容
        input.sendKeys(Keys.CONTROL, "a");
        Thread.sleep(2000);

       //ctrl+x 剪切输入框内容
        input.sendKeys(Keys.CONTROL, "x");
        Thread.sleep(2000);

       //ctrl+v 粘贴内容到输入框
        input.sendKeys(Keys.CONTROL, "v");
        Thread.sleep(2000);

      //通过回车键盘来代替点击操作
        input.sendKeys(Keys.ENTER);
        Thread.sleep(2000);
        //键盘输入F5
        input.sendKeys(Keys.F5);
        System.out.println("F5");
        driver.quit();
    }
}
