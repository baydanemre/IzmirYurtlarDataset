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

yurtlar.py: Veri setini oluşturmak için kullandığımız ana kod.
yurtlar_lokasyon.py: Veri setinin içindeki yurtların koordinatlarını otomasyon kullanarak almaya çalıştığımız kod.
	
	Yaşadığımız sorun: 

	Yurdun koordinat değerlerine sadece ,google maps üzerinde yurdun lokasyonunu gösteren kırmızı 
	raptiyenin göstgergesinin üzerine sağ tıklayarak erişebildik.Yani sitenin html kodu içerisinden bu
	değerlere erişmek imkansızdı.
	
	Çözüm:

	Google maps üzerinde bir yurt ismi arattığımızda, yukarıda belirttiğimiz kırmızı raptiye göstergesi, bilgisayar
	ekranının hep aynı noktasında beliriyordu,biz de selenium u "html içerisinden şu kod parçacğını bul ve click yap" 
	olarak kullanmak yerine "mouse ile laptop ekranımın şu koordinatlarını x ve y olarak al, ve bu spesifik x,y koordinatına
	sağ tık yap" şeklinde bir yaklaşım izledik.Çalıştı,yurtların yarısına yakınının koordinatını doğru bir şekilde aldık,
	fakat eğer gidilecek sıradaki yurt, o an ki yurttan çok uzaktaysa,google maps haritayı uzaklaştırıyor ve "ekranın
	belirttiğim koordinatına bas" mantığı burada işe yaramıyordu.

	Kullandığımız farklı modüller:
		
		pyautogui: Fare imlecimin ekran üzerindeki koordinatlarını görmek için kullandım.

		pyperclip: Yaptığımız son "kopyala" işleminin değerini alıp kod üzerindeki bir değişkene
		atamak için kullandık.
	

yurtlar_degisiklik.ipynb: 

	Yurdun veri seti üzerinde yer alan "yurt_ismi" adlı sütun değerleri üzerinden "yurt_ilce" adlı değişken ve değerlerini
	oluşturmak için kullandık.

	Yurdun veri seti üzerinde yer alan "yurt_ismi" adlı sütun değerleri üzerinden "yurt_cinsiyet" adlı değişken ve 
	değerlerini oluşturmak için kullandık.

	Yurdun veri seti üzerindeki bazı nümerik olmayan değerleri nümerik değere çevirmek için kullandık.
	
izmir_yurtlar_DF.xlsx:

	Yurtların verilerinin bulunduğu excel dosyasıdır.


VERİ SETİNİ OLUŞTURMAK İÇİN HANGİ PROGRAMLARDAN FAYDALANDIK

VISUAL STUDIO CODE:

	Kullandığımız yazılım dili: Python
	En çok Kullandığımız Modüller: Selenium,requests,beautifulsoup,pandas,time
		
		Selenium: Web scraping işlemi yapmak için kullandık.
		
		Pandas: Oluşturduğumuz sözlük yapılarını pandas dataframe'ine çevirmek ve bu dataframe'i
		excel veya csv dosyası olarak kaydetmek için kullandık.

		Time: Bu modülü,selenium kullanırken oluşacak olası hataları önlemek ve programın düzgün çalışması 
		için kullandık.
		
		Yaşadığımız sorun:
		
		Sitenin html kodu içinden istediğimiz değerleri requests ve beautifulsoup ile alamadık,
		alamama sebebimiz #text olarak gözüken değerlerin verisini çekemiyor olmamızdı,bu yüzden
		selenium ile çekmeye karar verdik.	


		Not2: Requests ve beautifulsoup modüllerini yardımcı olarak tuttuk,
		selenium ile çözemediğimiz bir durum olursa kullanmak için,fakat hiç kullanmadık.
		

MICROSOFT EXCEL:

	VS Code üzerinde oluşturduğumuz veri setlerini daha ayrıntılı görüp incelemek
	ve bazen de manuel olarak değişiklikler yapmak için kullandık.
		
FIREFOX:
	
	Verileri Firefox tarayıcı üzerinden çektik.

Terminal: 
	
	Karşılaştığımız çeşitli sorunlar için araştırma yaptığımızda, birkaç modüle ihtiyacımız
	olduğunun bilgisine ulaştık ve bu modülleri kullanabilmek için terminalde install
	işlemleri yaptık.

ChatGPT:

	Fare imlecimin laptop ekranım üzerindeki koordinat bilgilerini python ile hangi modülleri
	kullanarak alacağımız konusunda yardım aldık.
	
	Selenium webdriver'ının güncelleştirmesinin olup olmadığını,eğer varsa nasıl güncelleyeceğimizi
	öğrenmek için kullandık.


ÖDEVİ YAPARKEN YAŞADIĞIMIZ SORUNLAR:
	
	Yurtların fiyat bilgisi:
 
	Önce internet üzerinden bu verileri bulmaya çalıştık fakat çok tek tük bilgiler ve ortalama ne
	kadar olabileceği ile ilgili kesin olmayan fiyat bilgileri bulduk. Bornovadaki birkaç öğrenci yurduna mail
	attık.Fakat ya geri dönüş olmadı ya da bilgileri vermek istemediler.
	

KULLANDIĞIMIZ KAYNAKLAR

https://www.google.com/maps : Yurtların lokasyon değerlerini almak için kullandım.

Google bilgi kutucuğu: Yurtların ismi,adresi,no.su vb. gibi neredeyse bütün önemli verileri
çekmek için kullandım.

https://kygm.gsb.gov.tr/YurtMudurlukleri: Hangi yurtların devlet yurtları olduğu bilgisini teyit etmek
için kullandım.

https://www.yurtlarburada.com/izmir-ozel-ogrenci-yurtlari/: Site içerisinde yurtların kapasite değerleri yazdığından
verisetime ekleyebileceğim önemli verileri içeriyor. (Henüz eklemedim)


HAZIRLAYANLAR

İRFAN EMRE BAYDAN
SELENAY ÖZDEMİR

DOKUZ EYLÜL ÜNİVERSİTESİ - BİLGİSAYAR BİLİMLERİ 3. SINIF ÖĞRENCİLERİ



 

 