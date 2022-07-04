from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

URL = "https://www.linkedin.com/login?emailAddress=&fromSignIn=&trk=public_jobs_conversion-modal-signin&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_AL%3Dtrue%26keywords%3Dpython%2520developer%26sortBy%3DR"

us = "francoj.gallina@gmail.com"
ps = "linkedinfranco123!"

service = Service("C:\\Users\\Usuario\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(URL)

username = driver.find_element(By.ID, "username")
username.send_keys(us)
password = driver.find_element(By.ID, "password")
password.send_keys(ps)
login = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
login.click()

minimize = driver.find_element(By.XPATH, "/html/body/div[6]/aside/div[1]/header/div[3]/button[2]").click()

driver.implicitly_wait(5)

try:
    apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card .artdeco-button").click()
    apply2 = driver.find_element(By.CSS_SELECTOR, ".display-flex .artdeco-button--2").click()
    apply3 = driver.find_element(By.CSS_SELECTOR, ".display-flex .artdeco-button--primary").click()
    check = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/div/div/div/fieldset/div/div[1]/label").click()
    apply4 = driver.find_element(By.CSS_SELECTOR, ".display-flex .artdeco-button--primary").click()
    check2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[1]/label").click()
    apply5 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]/span").click()
except:
    print("click solicitud sencilla fallo")
