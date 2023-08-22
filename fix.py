from selenium import webdriver 
from selenium.webdriver.common.by import By
  
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
options.add_argument('--no-sandbox')

nama = "Aditya Erlangga"
username = "03041282025055@student.unsri.ac.id"
password_akun = "Keluargarn1"

mata_kuliah = dict()
mata_kuliah['SISTEM MIKROPROSESOR'] = "100196"
mata_kuliah['PENGOLAHAN SINYAL DIGITAL'] = "86664"
mata_kuliah['SISTEM KENDALI MULTIVARIABEL'] = "88997"
mata_kuliah['SISTEM KENDALI ADAPTIF'] = "94453"
mata_kuliah['SISTEM KENDALI OPTIMAL'] = "94576"

password = dict()
password['SISTEM KENDALI MULTIVARIABEL'] = "123456"
password['SISTEM KENDALI ADAPTIF'] = "123456"
password['SISTEM KENDALI OPTIMAL'] = "123456"

a = webdriver.Chrome(options=options)
a.maximize_window()
a.get('https://elearning.unsri.ac.id/')

a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[2]")[0].send_keys(username)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/input[3]")[0].send_keys(password_akun)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/button")[0].click()

result = '0'
def absen(key, value):
    a.get('https://elearning.unsri.ac.id/mod/attendance/view.php?id=' + value)
    tombol_absen = a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")#submit attendance
    if len(tombol_absen) > 0 :
        tombol_absen[0].click() #submit attendance
        if key == "SISTEM KENDALI MULTIVARIABEL" or key == "SISTEM KENDALI OPTIMAL" or key == "SISTEM KENDALI ADAPTIF":
            a.find_elements(By.ID, "id_studentpassword")[0].send_keys(password[key]) # password
            pasz = a.find_elements(By.ID, "id_studentpassword") # password
            status = a.find_elements(By.NAME, "status")
            if len(status) > 0:
                status[0].click()
            a.find_elements(By.ID, "id_submitbutton")[0].click()
            a.get('https://elearning.unsri.ac.id/mod/attendance/view.php?id=' + value)
            tombol_absen = a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")# cek lagi apakah masih submit attendance? kalo masih berarti password salah
            if len(tombol_absen) > 0 :
                report(key + "(gagal diabsen, password salah)")
            else:
                report(key + "(berhasil diabsen)")
        else:
            report(key + "(berhasil diabsen)")
            status = a.find_elements(By.NAME, "status") # present tombol
            if len(status) > 0:
                a.find_elements(By.NAME, "status")[0].click()
            a.find_elements(By.ID, "id_submitbutton")[0].click()
        print(key + ' => ABSEN ADA')
        global result
        result = '1'
    else :
        print(key + ' => ABSEN TIDAK ADA')

def report(text):
    a.get('https://absen.safesor.co.id/')
    a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/input")[0].send_keys(nama)
    a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/input")[0].send_keys(text)
    tombol = a.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div/form/div[2]/button")
    if(len(tombol)>0):
        tombol[0].click()

for key, value in mata_kuliah.items():
    absen(key, value)

if result == '0':
    report("Bot Masih Aktif")