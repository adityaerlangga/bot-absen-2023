from selenium import webdriver 
from selenium.webdriver.common.by import By
  
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
options.add_argument('--no-sandbox')

username = "your-username-or-email"
password = "your-password"

mata_kuliah = dict()
mata_kuliah['Matematika Teknik'] = "10364"
mata_kuliah['Dasar Sistem Kendali'] = "28973"
mata_kuliah['Metode Numerik'] = "11418"
mata_kuliah['Analisis Transien Rangkaian Listrik'] = "15035"
mata_kuliah['Sistem Kendali Terdistribusi'] = "16754"

a = webdriver.Chrome(options=options)
a.maximize_window()
a.get('https://elearning212.unsri.ac.id//')
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[4]/div/form/div[1]/input[4]")[0].send_keys(username)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[4]/div/form/div[1]/input[3]")[0].send_keys(password)
a.find_elements(By.XPATH,"/html/body/div[3]/header[1]/div/div/div[4]/div/form/div[1]/button")[0].click()

result = '0'
def absen(key, value):
    a.get('https://elearning212.unsri.ac.id/mod/attendance/view.php?id=' + value)
    tombol_absen = a.find_elements(By.XPATH,"//*[contains(texts(), 'Submit attendance')]")
    panjang = len(tombol_absen)
    if panjang > 0 :
        print(key + ' => ABSEN ADA')
        a.find_elements(By.XPATH,"//*[contains(texts(), 'Submit attendance')]")[0].click()
        a.find_elements(By.XPATH,"//*[contains(texts(), 'Present')]")[0].click()
        a.find_elements(By.XPATH,"//*[contains(texts(), 'Present')]")[0].click()
        a.find_element_by_id('id_submitbutton').click()
        result = key
    else :
        print(key + ' => ABSEN TIDAK ADA')

def total():
    a.get('https://wibowopedia.com/bot/home/index')
    a.find_elements(By.XPATH,"/html/body/header/div[2]/form/input[2]")[0].send_keys(result)
    tombol = a.find_elements(By.XPATH,"//*[contains(texts(), 'Button')]")
    if(len(tombol)>0):
        tombol[0].click()
    a.close()

for key, value in mata_kuliah.items():
    absen(key, value)

total()

