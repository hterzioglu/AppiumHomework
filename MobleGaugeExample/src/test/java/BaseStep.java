import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.touch.WaitOptions;
import io.appium.java_client.touch.offset.PointOption;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.support.ui.ISelect;

import java.nio.charset.MalformedInputException;
import java.time.Duration;
import java.util.List;
import java.util.Random;

public class  BaseStep extends BaseTest{

    @Step("<second> kadar bekle")
    public void waitForsecond(int second) throws InterruptedException {
        Thread.sleep(1000*second);
    }
    @Step("<Key> İd'li elemente tıkla")
    public void clickElementByid(String Key){
        appiumDriver.findElement(By.id(Key)).click();
        System.out.println(Key+"alısverise basla butonuna tıklandı tıklandı");
    }
    @Step("<Key> İd'li elemente <keywordc> değerini yaz")
    public void SendkeyElementByid(String Key,String keywordc){
        appiumDriver.findElement(By.id(Key)).sendKeys(keywordc);
        System.out.println(Key+"Elenitine tıklandı");

    }
    @Step("<Key> xpath'li elemente tıkla")
    public void clickElementByxpath(String Key){
        appiumDriver.findElement(By.xpath(Key)).click();
        System.out.println(Key+"Elenitine tıklandı");
    }
    @Step("<Key> xpath'li elemente <keywordc> değerini yaz")
    public void SendkeyElementByxpath(String Key,String keywordc){
        appiumDriver.findElement(By.xpath(Key)).sendKeys(keywordc);
        System.out.println(Key+"Elemente tıklandı");


    }

    /*@Step("Sayfayı yukarı kaydır")
    public void swipeUpI(){
        Dimension dims = appiumDriver.manage().window().getSize();
        System.out.println("Telefon Boyutu "+dims);
        PointOption pointOptionStart, pointOptionEnd;
        int edgeBorder = 10;
        final int PRESS_TIME = 200; // ms
        pointOptionStart = PointOption.point(dims.width / 2, dims.height / 2);
        System.out.println("pointOptionStart " + pointOptionStart);
        pointOptionEnd = PointOption.point(dims.width / 2, edgeBorder);
        System.out.println("pointOptionEnd " + pointOptionEnd);
        new TouchAction(appiumDriver)
                .press(pointOptionStart)
                // a bit more reliable when we add small wait
                .waitAction(WaitOptions.waitOptions(Duration.ofMillis(PRESS_TIME)))
                .moveTo(pointOptionEnd)
                .release().perform();
    } */
@Step("XpathElementi <xpath> bul ve <keyword> değerini kontrol et")
    public void textControl(String xpath,String keyword){
        System.out.println("Dogru acilan sayfada ki text degeri: " + appiumDriver.findElement(By.xpath(xpath)).getText());
        Assert.assertTrue("Text değeri bulunmamadı " ,appiumDriver.findElement(By.xpath(xpath)).getText().equals(keyword));
    }
    @Step("Sayfayı asagı kaydir")
    public void swipeDownI(){
        Dimension dims = appiumDriver.manage().window().getSize();
        System.out.println("telefon boyutu" + dims);
        PointOption pointOptionStart, pointOptionEnd;

        int edgeBorder = 20;
        final int PRESS_TIME = 200; // ms

        pointOptionStart = PointOption.point(dims.width / 4, dims.height / 2);
        System.out.println("pointoptionstar:" + pointOptionStart);
        pointOptionEnd = PointOption.point(dims.width / 2, edgeBorder);
        System.out.println("pointOptionEnd:"+ pointOptionEnd);
        new TouchAction(appiumDriver)
                .press(pointOptionStart)

                .waitAction(WaitOptions.waitOptions(Duration.ofMillis(PRESS_TIME)))
                .moveTo(pointOptionEnd)
                .release().perform();
        System.out.println("sayfa asagıya kaydirildi");



    }
    @Step("IdElementi <id> bul ve <keyword> değerini kontrol et")
    public void idControl(String id,String keyword){
        System.out.println("dogru sayfada ki elementin id si id si " + appiumDriver.findElement(By.xpath(id)).getText());
        Assert.assertEquals("Alışveriş sayfası bulunmadı " ,appiumDriver.findElement(By.xpath(id)).getText().equals(keyword));
    }
    @Step("random urun secme")
    public void randomlyClick(){

        List <MobileElement> randomPick =appiumDriver.findElements(By.xpath("//*[@resource-id='com.ozdilek.ozdilekteyim:id/imageView']"));
        Random random = new Random();
        int selectRandomInt =0;
        selectRandomInt = random.nextInt(randomPick.size());
        randomPick.get(selectRandomInt).click();




    }


    }



