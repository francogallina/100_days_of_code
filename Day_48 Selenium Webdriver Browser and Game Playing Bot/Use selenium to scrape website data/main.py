from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("C:\\Users\\Usuario\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
event_date = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
event_text = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')

events = {}

for n in range(len(event_text)):
    events[n] = {
        "time": event_date[n].text,
        "name": event_text[n].text,
    }

print(events)

"""Cerrar la pesaña abierta"""
driver.close()

"""Cerrar todas las pestañas"""
# driver.quit()

