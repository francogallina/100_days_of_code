from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("C:\\Users\\Usuario\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element(By.NAME, "fName")
firstName.send_keys("Franco")
lastName = driver.find_element(By.NAME, "lName")
lastName.send_keys("Gallina")
email = driver.find_element(By.NAME, "email")
email.send_keys("franco@hotmail.com")

button = driver.find_element(By.CLASS_NAME, "btn-lg")
# button = driver. find_element(By.CSS_SELECTOR, "form button")     Otra forma de hacerlo
button.click()

