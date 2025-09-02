
#starter code for selenium & webdriver installation & setup basic browser task --- IGNORE ---
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# website = "https://www.adamchoi.co.uk/overs/detailed"
# path = r"C:\chromedriver\chromedriver.exe"   # <-- full path to chromedriver.exe
# service = Service(path)
# driver = webdriver.Chrome(service=service)
# driver.get(website)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\chromedriver\chromedriver.exe"   # <-- full path to chromedriver.exe
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(website)
#Clicking a 
all_matches_button = driver.find_element(
    By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

import time
# ... your code ...
time.sleep(30)   # keeps browser open for 20 seconds
