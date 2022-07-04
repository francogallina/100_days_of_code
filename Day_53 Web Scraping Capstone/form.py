from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfqTwssZUKcs5XOXoRAXnl2pN-kIYlRYA9pGsNToMkwG7wpSA/viewform?usp=sf_link"

class rellenar_formulario:
    def __init__(self, path):
        self.service = Service(path)
        self.driver = webdriver.Chrome(service= self.service)

    def rellenar(self, address, price, link):
        self.driver.get(GOOGLE_FORM)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/"
                                           "div/div[1]/input").send_keys(address)
        self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/"
                                           "div/div[1]/input").send_keys(price)
        self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/"
                                           "div/div[1]/input").send_keys(link)
        self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
