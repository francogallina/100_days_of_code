from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time


PROMISED_DOWN = 50
PROMISED_UP = 15
CHROME_DRIVER_PATH = "C:\\Users\\Usuario\\Development\\chromedriver.exe"
URL = "https://twitter.com/home"


class InternetSpeedTwitterBot():
    def __init__(self, path):
        self.service = Service(path)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/13278007579")
        self.go = self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(60)
        self.data = self.driver.find_elements(By.CLASS_NAME, "result-data-large")
        self.up = self.data[1].text
        self.down = self.data[2].text
        return self.up
        return  self.down


    def tweet_at_provider(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://twitter.com")
        time.sleep(5)
        self.driver.implicitly_wait(20)
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/"
                                           "div[1]/div/div[3]/div[5]/a/div/span/span").click() # INICIAR SESION
        except:
            self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[2]/"
                                               "div[4]/div[2]/span/span").click()  # INICIAR SESION
        self.driver.find_element(By.NAME, "text").send_keys("francoj.gallina@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/" \
                                            "div[2]/div[2]/div/div/div/div[6]/div/span/span").click() # SIGUIENTE
        self.driver.find_element(By.NAME, "password").send_keys("twitterPython2005!")
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()  # INICIAR

        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/"
                                               "div/div/div/div/div/div[2]/div[4]/div").click()
        except:
            pass
        twit = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        twit.send_keys(f"Internet speed {self.up} up / {self.down} down")
        twit.send_keys(Keys.ENTER)



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
time.sleep(10)
print(bot.down)
print(bot.up)
bot.tweet_at_provider()


#No esta terminado - De tanto intentar me pide verificación