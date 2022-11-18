
from PIL import Image
from numpy import asarray
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# HSSport credentials
username = "mg272@uni-heidelberg.de"
password = "j9GqqJrCrSarZp"

# initialize the Firefox driver
driver = webdriver.Firefox()

# Anmelden
driver.get("https://hochschulsport.uni-heidelberg.de/oa_oeff/login.php")
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("passw").send_keys(password)
driver.find_element_by_name("submit1").click()

# Auf Ticketseite gehen
driver.get("https://hochschulsport.uni-heidelberg.de/oa_oeff/qr_rubriken.php")

# Den n-ten Submit Knopf drücken (form[n])
#Badminton - Freies Spiel 4 (CARD) (bezahlter Kurs), n = 1

#Badminton - Freies Spiel 5 (CARD) (bezahlter Kurs), n = 2

#Basketball - Freies Spiel 2 (CARD) (bezahlter Kurs), n = 3

#Futsal - Freies Spiel 2 (CARD) (bezahlter Kurs), n = 4

#Baseball / Softball (CARD) (bezahlter Kurs), n = 5

#Volleyball - 50:50 (CARD) (bezahlter Kurs), n = 6

#Volleyball - Freies Spiel 2 (CARD) (bezahlter Kurs), n = 7

driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div[1]/span/form[2]/input[1]").click()

# Screenshot nehmen
driver.save_screenshot("/Users/sebastianmetzler/Desktop/notebooks/vscode/screenshot.png")

# Bild croppen
source_img = Image.open('/Users/sebastianmetzler/Desktop/notebooks/vscode/screenshot.png')
data = asarray(source_img)
crop_data = data[690:735,  515:640]
crop_img = Image.fromarray(crop_data)
crop_img.save("/Users/sebastianmetzler/Desktop/notebooks/vscode/cropped.png", format="png")

# Bild analysieren
os.system("tesseract /Users/sebastianmetzler/Desktop/notebooks/vscode/cropped.png out")

with open("out.txt", "r") as file:
    data = file.read()
print(data)    
print(eval(data)) # Ausrechnen

# Einsetzen in Captcha und abschicken! :)
driver.find_element_by_name("sicherheitscode").send_keys(str(eval(data)))
driver.find_element_by_name("buchen").click()
