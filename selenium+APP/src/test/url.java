package test;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class url {
    public static void main(String[] args) throws Exception {
        System.out.println("开始！");
        Pattern pattern = Pattern.compile("http(s)?://([\\w-]+\\.)+[\\w-]+(/[\\w- ./?%&=]*)?");
        URL baidu = new URL("http://www.cnblogs.com/A--Q/");
        BufferedReader br = new BufferedReader(new InputStreamReader(baidu.openStream(), "utf-8"));
        String inputLine;
        while ((inputLine = br.readLine()) != null) {
            Matcher matcher = pattern.matcher(inputLine);
            while (matcher.find()) {
                System.out.println(matcher.group(0));
            }
        }
        br.close();
        System.out.println("程序执行结束！");
    }
}