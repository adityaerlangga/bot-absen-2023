from selenium import webdriver 
from selenium.webdriver.common.by import By
  
a = webdriver.Chrome('C:\Program Files\Chromedriver\chromedriver.exe')

nama = "Aditya Erlangga"
username = "03041282025055@student.unsri.ac.id"
password = "Keluargarn1"

mata_kuliah = dict()
mata_kuliah['SISTEM MIKROPROSESOR'] = "100196"
mata_kuliah['PENGOLAHAN SINYAL DIGITAL'] = "86664"
mata_kuliah['SISTEM KENDALI MULTIVARIABEL'] = "88997"
mata_kuliah['SISTEM KENDALI OPTIMAL'] = "94576"
mata_kuliah['SISTEM KENDALI ADAPTIF'] = "94453"

a.maximize_window()
a.get('https://elearning.unsri.ac.id/')

a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[2]")[0].send_keys(username)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[3]")[0].send_keys(password)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/button")[0].click()

result = '0'
def absen(key, value):
    a.get('https://elearning.unsri.ac.id/mod/attendance/view.php?id=' + value)
    tombol_absen = a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")
    panjang = len(tombol_absen)
    if panjang > 0 :
        print(key + ' => ABSEN ADA')
        a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")[0].click()
        a.find_elements(By.XPATH,"//*[contains(text(), 'Present')]")[0].click()
        a.find_element_by_id('id_submitbutton').click()
        result = key
        total()
    else :
        print(key + ' => ABSEN TIDAK ADA')

def total():
    a.get('https://absen.safesor.co.id/')
    a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/input")[0].send_keys(nama)
    if result == '0':
        a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/input")[0].send_keys("0")
    else:
        a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/input")[0].send_keys(result)
    tombol = a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[2]/button")
    if(len(tombol)>0):
        tombol[0].click()
    a.close()

for key, value in mata_kuliah.items():
    absen(key, value)

total()