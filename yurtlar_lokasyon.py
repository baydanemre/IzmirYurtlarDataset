from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pyautogui
import pyperclip

""" while True:
    x, y = pyautogui.position()
    print(f"Fare imlecinin koordinatları: X={x}, Y={y}") """

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://www.google.com/maps/@38.4285987,27.1852937,15z?entry=ttu")
time.sleep(5)

excel_file_path = "yurtlar_data_new_3.xlsx"  # Dosya adını ve yolunu ayarlayın
df = pd.read_excel(excel_file_path)

yurt_lokasyon = list()
lokasyon_dict = {}

for i in range(0,len(df)):
    yurt_isim = df["yurt_ismi"][i]
    search_box = driver.find_element(By.CSS_SELECTOR,"#searchboxinput")
    search_box.send_keys(yurt_isim)
    tikla_buton = driver.find_element(By.CSS_SELECTOR,"#searchbox-searchbutton")
    tikla_buton.click()
    time.sleep(2)

    if(i>1):
        if(i==2):
            x = 1006
            y = 350
            action_chains = ActionChains(driver)
            action_chains.move_by_offset(x, y).context_click().perform()
            time.sleep(1)
            action_chains.move_by_offset(20, 20).click().perform()
            copied_text = pyperclip.paste()
            yurt_lokasyon.append(copied_text)

        else:
            x=0
            y=0
            action_chains = ActionChains(driver)
            action_chains.move_by_offset(-20, -20).context_click().perform()
            time.sleep(1)
            action_chains.move_by_offset(20, 20).click().perform()
            copied_text = pyperclip.paste()
            yurt_lokasyon.append(copied_text)

    
    search_box.clear()

for i in range(0,len(yurt_lokasyon)):
    print(yurt_lokasyon[i])

lokasyon_dict = {"yurt_lokasyon":lokasyon_dict}
lokasyonlar = pd.DataFrame(lokasyon_dict)

dosya_adi = "yurtlar_lokasyon.xlsx"
lokasyonlar.to_excel(dosya_adi,sheet_name="Yurt_Lokasyon", index=False)
