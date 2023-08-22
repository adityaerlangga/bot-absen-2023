from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
  
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
options.add_argument('--no-sandbox')

nama = "Aditya Erlangga"
username = "03041282025055@student.unsri.ac.id"
password_akun = "kuliah_unsri_2020"

mata_kuliah = dict()
mata_kuliah['SISTEM MIKROPROSESOR'] = "100196"
mata_kuliah['PENGOLAHAN SINYAL DIGITAL'] = "86664"
mata_kuliah['SISTEM KENDALI MULTIVARIABEL'] = "88997"
mata_kuliah['SISTEM KENDALI ADAPTIF'] = "94453"
mata_kuliah['SISTEM KENDALI OPTIMAL'] = "94576"
mata_kuliah['SISTEM BASIS DATA'] = "103670"
mata_kuliah['PEMROGRAMAN LANJUT'] = "103688"

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
        if key == "S":
            input_pass = a.find_elements(By.ID, "id_studentpassword")
            if len(input_pass) > 0:
                input_pass[0].send_keys(password[key])
            status = a.find_elements(By.NAME, "status")
            if len(status) > 0:
                status[0].click()
            btnsubmit = a.find_elements(By.ID, "id_submitbutton")
            if len(btnsubmit) > 0:
                btnsubmit[0].click()
            a.get('https://elearning.unsri.ac.id/mod/attendance/view.php?id=' + value)
            new_tombol_absen = a.find_elements(By.XPATH,"//*[contains(text(), 'Submit attendance')]")# cek lagi apakah masih submit attendance? kalo masih berarti password salah
            if len(new_tombol_absen) > 0 :
                report(key + "(gagal diabsen, password salah)")
            else:
                report(key + "(berhasil diabsen)")
        else:
            # time.sleep(1) ###########SLEEP###########
            status = a.find_elements(By.NAME, "status") # present tombol
            if len(status) > 0:
                status[0].click()
            submit = a.find_elements(By.ID, "id_submitbutton")
            if len(submit) > 0:
                submit[0].click()
            report(key + "(berhasil diabsen)")
        # print(key + ' => ABSEN ADA')
        global result
        result = '1'
    else :
        print(key + ' => ABSEN TIDAK ADA')

def report(mata_kuliah):
    a.get('https://absen.safesor.co.id/form')
    input_nama = a.find_elements(By.ID, "nama")
    if(len(input_nama)>0):
        input_nama[0].send_keys(nama)
    input_mata_kuliah = a.find_elements(By.ID, "mata_kuliah")
    if(len(input_mata_kuliah)>0):
        input_mata_kuliah[0].send_keys(mata_kuliah)
    tombol_submit_report = a.find_elements(By.ID, "submit-button")
    if(len(tombol_submit_report)>0):
        tombol_submit_report[0].click()


for key, value in mata_kuliah.items():
        absen(key, value)

if result == '0':
    report("Bot Masih Aktif")