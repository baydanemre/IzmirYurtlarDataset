VERİ SETİNİN DEĞİŞKEN İSİMLENDİRMELERİ

yurt_ilce: Yurdun hangi ilçede olduğunu gösterir.
yurt_ismi: Yurdun google maps üzerinde kayıtlı olan ismini gösterir.
yurt_cinsiyet: Yurdun hangi cinsiyette öğrenci barındırdığını söyler.
yurt_kategori: Yurdun ozel mi devlet mi yoksa vakıf mı olduğunun bilgisini verir.
yurt_puan: Yurdun google değerlendirme puanıdır.
yurt_degerlendirme_sayisi: Yurdun google değerlendirme sayısıdır.
yurt_saat: Yurdun 24 saat açık olup olmadığını ve geçici olarak kapalı olduğunun bilgisini verir.( " - " işareti 24 saat açık olmadığı anlamına gelir.)
yurt_tel: Yurdun iletişim numarasıdır.
yurt_adres: Yurdun açık adresidir.
yurt_website: Yurt eğer bir websitesine sahip ise websitesini,değil ise " - " değerini gösterir.
yurt_enlem: Yurdun google maps koordinatlarındaki enlem değerini verir.
yurt_boylam: Yurdun google maps koordinatlarındaki boylam değerini verir.

PROJE DOSYALARI

yurtlar.py: Veri setini oluşturmak için kullandığım ana kod.
yurtlar_lokasyon.py: Veri setinin içindeki yurtların koordinatlarını otomasyon kullanarak almaya çalıştığım kod.
	
	Yaşadığım sorun: 

	Yurdun koordinat değerlerine sadece ,google maps üzerinde yurdun lokasyonunu gösteren kırmızı 
	raptiyenin göstgergesinin üzerine sağ tıklayarak erişebildim.Yani sitenin html kodu içerisinden bu
	değerlere erişmek imkansızdı.
	
	Çözüm:

	Google maps üzerinde bir yurt ismi arattığımda, yukarıda belirttiğim kırmızı raptiye göstergesi, bilgisayar
	ekranımın hep aynı noktasında beliriyordu,ben de selenium u "html içerisinden şu kod parçacğını bul ve click yap" 
	olarak kullanmak yerine "mouse ile laptop ekranımın şu koordinatlarını x ve y olarak al, ve bu spesifik x,y koordinatına
	sağ tık yap" şeklinde bir yaklaşım izledim.Çalıştı,yurtlarının yarısına yakınının koordinatını doğru bir şekilde aldım,
	fakat eğer gidilecek sıradaki yurt, o an ki yurttan çok uzaktaysa,google maps haritayı uzaklaştırıyor ve "ekranın
	belirttiğim koordinatına bas" mantığı burada işe yaramıyordu.

	Kullandığım farklı modüller:
		
		pyautogui: Fare imlecimin ekran üzerindeki koordinatlarını görmek için kullandım.

		pyperclip: Yaptığım son "kopyala" işleminin değerini alıp kodum üzerindeki bir değişkene
		atamak için kullandım.
	

yurtlar_degisiklik.ipynb: 

	Yurdun veri seti üzerinde yer alan "yurt_ismi" adlı sütun değerleri üzerinden "yurt_ilce" adlı değişken ve değerlerini
	oluşturmak için kullandım.

	Yurdun veri seti üzerinde yer alan "yurt_ismi" adlı sütun değerleri üzerinden "yurt_cinsiyet" adlı değişken ve 
	değerlerini oluşturmak için kullandım.

	Yurdun veri seti üzerindeki bazı nümerik olmayan değerleri nümerik değere çevirmek için kullandım.
	



VERİ SETİNİ OLUŞTURMAK İÇİN HANGİ PROGRAMLARDAN FAYDALANDIM

VISUAL STUDIO CODE:

	Kullandığım yazılım dili: Python
	En çok Kullandığım Modüller: Selenium,requests,beautifulsoup,pandas,time
		
		Selenium: Web scraping işlemi yapmak için kullandım.
		
		Pandas: Oluşturduğum sözlük yapılarını pandas dataframe'ine çevirmek ve bu dataframe'i
		excel veya csv dosyası olarak kaydetmek için kullandım.

		Time: Bu modülü,selenium kullanırken oluşacak olası hataları önlemek ve programın düzgün çalışması 
		için kullandım.
		
		Yaşadığım sorun:
		
		Sitenin html kodu içinden istediğim değerleri requests ve beautifulsoup ile alamadım,
		alamama sebebim. #text olarak gözüken değerlerin verisini çekemiyor olmamdı,bu yüzden
		selenium ile çekmeye karar verdim.	


		Not2: Requests ve beautifulsoup modüllerini yardımcı olarak tuttum,
		selenium ile çözemediğim bir durum olursa kullanmak için,fakat hiç kullanmadım.
		

MICROSOFT EXCEL:

	VS Code üzerinde oluşturduğum veri setlerini daha ayrıntılı görüp incelemek
	ve bazen de manuel olarak değişiklikler yapmak için kullandım.
		
FIREFOX:
	
	Verileri Firefox tarayıcı üzerinden çektim.

Terminal: 
	
	Karşılaştığım çeşitli sorunlar için araştırma yaptığımda, birkaç modüle ihtiyacım
	olduğunun bilgisine ulaştım ve bu modülleri kullanabilmek için terminalde install
	işlemleri yaptım.

ChatGPT:

	Fare imlecimin laptop ekranım üzerindeki koordinat bilgilerini python ile hangi modülleri
	kullanarak alacağım konusunda yardım aldım.
	
	Selenium webdriver'ının güncelleştirmesinin olup olmadığını,eğer varsa nasıl güncelleyeceğimi
	öğrenmek için kullandım.


ÖDEVİ YAPARKEN YAŞADIĞIM SORUNLAR:
	
	Yurtların fiyat bilgisi:
 
	Önce internet üzerinden bu verileri bulmaya çalıştım fakat çok tek tük bilgiler ve ortalama ne
	kadar olabileceği ile ilgili kesin olmayan fiyat bilgileri buldum. Arkadaşım ile bornovadaki birkaç öğrenci yurduna mail
	attık.Fakat ya geri dönüş olmadı ya da bilgileri vermek istemediler.
	

KULLANDIĞIM KAYNAKLAR

https://www.google.com/maps : Yurtların lokasyon değerlerini almak için kullandım.

Google bilgi kutucuğu: Yurtların ismi,adresi,no.su vb. gibi neredeyse bütün önemli verileri
çekmek için kullandım.

https://kygm.gsb.gov.tr/YurtMudurlukleri: Hangi yurtların devlet yurtları olduğu bilgisini teyit etmek
için kullandım.

https://www.yurtlarburada.com/izmir-ozel-ogrenci-yurtlari/: Site içerisinde yurtların kapasite değerleri yazdığından
verisetime ekleyebileceğim önemli verileri içeriyor. (Henüz eklemedim)




 

 