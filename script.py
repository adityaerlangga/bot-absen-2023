from selenium import webdriver
from pprint import pprint
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.5)
driver.get("https://wibowopedia.com/bot/")
#identify element
l= driver.find_elements(By.XPATH,"//*[contains(text(), 'Buttonz')]")
s = len(l)
#get list size with len
# l.click()
# check condition, if list size > 0, element exists
if (s>0):
    print("Element exist")
else :
    print("Element does not exist")
driver.close()