from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


URL = "https://tinder.com/app/recs"
service = Service("C:\\Users\\Usuario\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(URL)
time.sleep(5)
cookies = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button").click()
login = driver.find_element(By.CLASS_NAME, "button").click()


time.sleep(5)
login_with_facebook = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]").click()

time.sleep(5)
tinder_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]

driver.switch_to.window(facebook_login_window)

email = driver.find_element(By.ID, "email").send_keys("franco_049@hotmail.com")
password = driver.find_element(By.ID, "pass").send_keys("francoFacebook123!")
login = driver.find_element(By.NAME, "login").click()

driver.switch_to.window(tinder_window)

time.sleep(5)
ubication = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
notifications = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]").click()


#Hit Like
for n in range(100):
    time.sleep(5)

    try:
        like = driver.find_element(By.XPATH, "//button[@data-testid='gamepadLike']").click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()

        except NoSuchElementException:
            time.sleep(2)

