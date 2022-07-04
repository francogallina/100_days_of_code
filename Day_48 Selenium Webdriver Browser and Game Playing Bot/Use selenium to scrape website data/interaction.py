from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("C:\\Users\\Usuario\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

"""Buscar un elemento e imprimirlo"""
# number_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(number_articles.text)

"""Con find_element by link_text se busco un link con el nombre designado"""
# all_portals = driver.find_element(By.LINK_TEXT, "Community portal").click()

"""Buscar la barra de busqueda y compeltarla"""
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER) #search.submit()   Busca resultados de otra manera, ni idea cual
