Getting Started with Gauge
==========================

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, use `mvn test`

Wait
--------
* "3" kadar bekle
* XpathElementi "//*[@text='ALIŞVERİŞE BAŞLA']" bul ve "ALIŞVERİŞE BAŞLA" değerini kontrol et
* "3" kadar bekle


AlısverisButtonClick
---
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* XpathElementi "//*[@text='Ev Tekstili']" bul ve "Ev Tekstili" değerini kontrol et
* "3" kadar bekle

KategorilerButtonClick
-------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* XpathElementi "//*[@text='Kadın']" bul ve "Kadın" değerini kontrol et
* "3" kadar bekle

CategoryWomenSelect
------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle

CategoryWomenTojeanSelect
--------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
SwipeDown
--------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle

SelectProductRandom
----------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* random urun secme
* "3" kadar bekle
* XpathElementi "//*[@text='SEPETE EKLE']" bul ve "SEPETE EKLE" değerini kontrol et
* "3" kadar bekle

ClickFavoriteButton
------------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* random urun secme
* "3" kadar bekle
* XpathElementi "//*[@text='SEPETE EKLE']" bul ve "SEPETE EKLE" değerini kontrol et
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/imgFav']" xpath'li elemente tıkla
* "3" kadar bekle

LoginButton
----------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* random urun secme
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/imgFav']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='E - posta Adresi']" xpath'li elemente "hayrettin.terzioglu@testinium.com" değerini yaz
* "3" kadar bekle
* "//*[@text='Parola']" xpath'li elemente "testData" değerini yaz
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/btnLogin" İd'li elemente tıkla
* "3" kadar bekle



ClickBackButton1
-------------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* random urun secme
* "3" kadar bekle
* XpathElementi "//*[@text='SEPETE EKLE']" bul ve "SEPETE EKLE" değerini kontrol et
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/imgFav']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='E - posta Adresi']" xpath'li elemente "hayrettin.terzioglu@testinium.com" değerini yaz
* "3" kadar bekle
* "//*[@text='Parola']" xpath'li elemente "testData" değerini yaz
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/btnLogin" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/ivBack']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/ivBack']" xpath'li elemente tıkla
* "3" kadar bekle

randomProductSelectAndAddCart
--------------------
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" İd'li elemente tıkla
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Kadın']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='Pantolon']" xpath'li elemente tıkla
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* Sayfayı asagı kaydir
* "3" kadar bekle
* random urun secme
* "3" kadar bekle
* XpathElementi "//*[@text='SEPETE EKLE']" bul ve "SEPETE EKLE" değerini kontrol et
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/imgFav']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@text='E - posta Adresi']" xpath'li elemente "hayrettin.terzioglu@testinium.com" değerini yaz
* "3" kadar bekle
* "//*[@text='Parola']" xpath'li elemente "testData" değerini yaz
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/btnLogin" İd'li elemente tıkla
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/ivBack']" xpath'li elemente tıkla
* "3" kadar bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/ivBack']" xpath'li elemente tıkla
* "3" kadar bekle
* random urun secme
* "3" kadar bekle
* "com.ozdilek.ozdilekteyim:id/ivAddCart" İd'li elemente tıkla
* "3" kadar bekle







