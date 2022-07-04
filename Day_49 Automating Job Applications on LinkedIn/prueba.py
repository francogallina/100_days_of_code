from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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

try:
    minimize = driver.find_element(By.XPATH, "/html/body/div[6]/aside/div[1]/header/div[3]/button[2]").click()

    id_jobs = []
    jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list li")
    for i in jobs:
        if i.get_attribute("id") != "":
            id_jobs.append(i.get_attribute("id"))

    for i in id_jobs:
        time.sleep(5)
        try:
            apply_job = driver.find_element(By.ID, i).click()
            apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card .artdeco-button").click()

            apply2 = driver.find_element(By.CSS_SELECTOR, ".display-flex .artdeco-button--2")

            if apply2.get_attribute("aria-label") == "Ir al siguiente paso":
                print("Paso siguiente no deseado - se procede a cerrrar")
                close_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button/li-icon").click()
                descartar_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]").click()
            else:
                apply2 = driver.find_element(By.CSS_SELECTOR, ".display-flex .artdeco-button--2").click()
        except:
            print("click solicitud sencilla fallo")
except:
    driver.refresh()
# Incompleto, no quise llenar linkedin de guardados y empresas seguidas. Y postularse a cada una tiene preguntas diferentes.


