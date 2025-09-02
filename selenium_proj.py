from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\chromedriver\chromedriver.exe"   # <-- full path to chromedriver.exe
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(website)

driver.quit()