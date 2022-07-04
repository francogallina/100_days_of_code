from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "khloekardashian"
USERNAME = "francogallina@hotmail.es"
PASSWORD = "instagramPython2005!"

class InstaFollower:
    def __init__(self, path):
        self.service = Service(path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get(URL)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.NAME, 'username').send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        try:
            self.driver.find_element(By.XPATH, "//div[@class='cmbtv']/button").click()
        except:
            pass
        try:
            self.driver.find_element(By.XPATH, "//div[@class='_a9-z']/button[2]").click()
        except:
            pass

    def find_followers(self):
        self.driver.get("https://www.instagram.com/khloekardashian/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(5)

        for i in range(10):
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/"
                                               "div/div/div/div/div/div/div/div[2]/ul/div//li//a").send_keys(Keys.END)
            time.sleep(2)


    def follow(self):
        self.list_follower = self.driver.find_elements(By.CLASS_NAME, "_aaes")

        for self.x in self.list_follower:
           try:
               self.x.click()
               time.sleep(1)
           except ElementClickInterceptedException:
               pass
