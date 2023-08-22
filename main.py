# from datetime import date, datetime
from pprint import pprint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException      
from selenium.webdriver.common.by import By  
# import os
import time

# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# time.sleep(60)

username = "03041282025055@student.unsri.ac.id"
password = "Keluargarn1"

mata_kuliah = dict()
mata_kuliah['Matematika Teknik'] = "10261"
mata_kuliah['Dasar Sistem Kendali'] = "28960"
mata_kuliah['Metode Numerik'] = "11418"
mata_kuliah['Analisis Transien Rangkaian Listrik'] = "15033"

a = webdriver.Chrome(options=options)
a.maximize_window()
a.get('https://elearning212.unsri.ac.id//')
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[2]")[0].send_keys(username)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[3]")[0].send_keys(password)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/button")[0].click()

result = '0'
def absen(key, value):
    a.get('https://elearning212.unsri.ac.id/mod/attendance/view.php?id=' + value)
    tombol_absen = a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")
    panjang = len(tombol_absen)
    if panjang > 0 :
        print(key + ' => ABSEN ADA')
        a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")[0].click()
        a.find_elements(By.XPATH,"//*[contains(text(), 'Present')]")[0].click()
        a.find_elements(By.XPATH,"//*[contains(text(), 'Present')]")[0].click()
        a.find_element_by_id('id_submitbutton').click()
        result = key
    else :
        print(key + ' => ABSEN TIDAK ADA')

def total():
    a.get('https://wibowopedia.com/bot/home/index')
    a.find_elements(By.XPATH,"/html/body/header/div[2]/form/input[2]")[0].send_keys(result)
    tombol = a.find_elements(By.XPATH,"//*[contains(text(), 'Button')]")
    if(len(tombol)>0):
        tombol[0].click()
    a.close()


for key, value in mata_kuliah.items():
    absen(key, value)
    # print(key, " => ", value)

total()

