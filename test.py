from selenium import webdriver

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
driver.get("https://")