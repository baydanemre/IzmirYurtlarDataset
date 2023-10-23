from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium.webdriver.firefox.service import Service

gecko_driver_path = r"C:\Users\Lenovo\Downloads\geckodriver.exe"
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

def cevir(metin):
    turkce_karakterler = "ÇçĞğİıÖöŞşÜü"
    ingilizce_karakterler = "CcGgIiOoSsUu"
    ceviri_tablosu = str.maketrans(turkce_karakterler, ingilizce_karakterler)
    metin = metin.translate(ceviri_tablosu)

    return metin.replace("(","").replace(")","").lower()


Headers={"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}

driver.get("https://www.google.com/search?sca_esv=575589114&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=AM9HkKnfPEjxRv7PSfNIuDdAW4gvJFzfhw:1697975816174&q=izmir+yurtlar&rflfq=1&num=10&sa=X&ved=2ahUKEwimyvDqzImCAxXBIUQIHcF0Bm8QjGp6BAgREAE&biw=1536&bih=731&dpr=1.25#rlfi=hd:;si:;mv:[[38.4762488,27.2440283],[38.3690661,27.122457999999998]]")
time.sleep(5)

yurt_puan = list()
yurt_degerlendirme_sayisi = list()
yurt_isim = list()
yurt_website = list()
yurt_tel = list()
yurt_saat = list()
yurt_adres = list()
yurt_cinsiyet = list()
yurt_kategori = list()
yurt_ilkyorum = list()

# .AaVjTc > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) 2
#.AaVjTc > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) 3
#.AaVjTc > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5)


for i in range(0,1):
    #Sayfalar arası gezmek için gerekli kodu yaz.
    sayfa_gezme=driver.find_element(By.CSS_SELECTOR,f".AaVjTc > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child({i+3})")
    sayfa_gezme.click()
    time.sleep(3)
    
    #/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div
    #/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[6]/div[2]/div/div
    #/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[8]/div[2]/div/div
    #/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div
    #/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[6]/div[2]/div/div
    for i in range(0,3):
        try:
            yurt_info = driver.find_element(By.XPATH , f"/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{4+(i*2)}]/div[2]/div/div")
            yurt_info.click()
            time.sleep(2) 
        except NoSuchElementException:
            continue

        try:
            yurt_puan.append(cevir(driver.find_element(By.CSS_SELECTOR , ".CJQ04 > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text))
        except NoSuchElementException:
            yurt_puan.append("-")

        try:
            yurt_degerlendirme_sayisi.append(cevir(driver.find_element(By.CSS_SELECTOR,".CJQ04 > div:nth-child(1) > span:nth-child(1) > span:nth-child(3)").text))

        except NoSuchElementException:
            yurt_degerlendirme_sayisi.append("-")

        try:
            website_varmi = driver.find_element(By.CSS_SELECTOR, ".zhZ3gf > div:nth-child(1) > a:nth-child(1)")
            yurt_website.append(website_varmi.get_attribute("href"))
        except NoSuchElementException:
            yurt_website.append("-")

        try:
            yurt_varmi=driver.find_element(By.CSS_SELECTOR,".farUxc > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
            yurt_adres.append(cevir(yurt_varmi.text))
            new_text = yurt_varmi.text.replace("Adres: ", "")
        except NoSuchElementException:
            yurt_adres.append("-")    



        try:
            tel_varmi = driver.find_element(By.CSS_SELECTOR,"span.LrzXr:nth-child(1) > a:nth-child(1) > span:nth-child(1)")
            yurt_tel.append(cevir(tel_varmi.text))
        except NoSuchElementException:
            yurt_tel.append("-")


        try:
            yurt_saati = driver.find_element(By.XPATH,f"/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{4+(i*2)}]/div[2]/div/div/a/div/div/div[4]").text
            yurt_saat.append(cevir(yurt_saati))
        except NoSuchElementException:
            yurt_saat.append("-")

        yurt_ismi = driver.find_element(By.CSS_SELECTOR,".qrShPb > span:nth-child(1)").text
        yurt_isim.append(cevir(yurt_ismi))


for i in yurt_isim:
    if("erkek" in i):
        yurt_cinsiyet.append("erkek")
    elif("kiz" in i):
        yurt_cinsiyet.append("kiz")
    else:
        yurt_cinsiyet.append("-")

for i in yurt_isim:
    if("ozel" in i):
        yurt_kategori.append("ozel")
    else:
        yurt_kategori.append("-")

for i in range(0,len(yurt_saat)):
    if("24" in yurt_saat[i]):
        yurt_saat[i] = "24 saat acik"
    elif("gecici" in yurt_saat[i]):#
        yurt_saat[i] = "gecici olarak kapali"
    else:
        yurt_saat[i] = "-"

yurtlar_dataset = {"yurt_ismi":yurt_isim
                ,"yurt_cinsiyet":yurt_cinsiyet 
                ,"yurt_kategori":yurt_kategori
                ,"yurt_puan":yurt_puan 
                ,"yurt_degerlendirme":yurt_degerlendirme_sayisi 
                ,"yurt_saat": yurt_saat
                ,"yurt_tel":yurt_tel
                ,"yurt_adres": yurt_adres
                ,"yurt_website":yurt_website}

yurtlar_dataframe = pd.DataFrame(yurtlar_dataset)
print(yurtlar_dataframe) 



""" dosya_adi = "izmir_yurtlar_DF.xlsx"
yurtlar_dataframe.to_excel("selenay.xlsx",sheet_name="selenay_verileri",index=False) """

#/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div
#/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div
#/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div

#/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/a[1]
#/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[6]/div[2]/div/a[1]
#/html/body/div[4]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[16]/div[2]/div/a[1]

#.zhZ3gf > div:nth-child(1) > a:nth-child(1)
#.zhZ3gf > div:nth-child(1) > a:nth-child(1)
