from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\Users\\Usuario\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 60*5
time_to_shop = time.time() + 5

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > time_to_shop:
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        items_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                items_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(items_prices)):
            cookie_upgrades[items_prices[n]] = items_id[n]

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",","")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        time_to_shop = time.time() + 5


    if time.time() > timeout:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break













# cursor = driver.find_element(By.ID, "buyCursor")
# grandma = driver.find_element(By.ID, "buyGrandma")
# factory = driver.find_element(By.ID, "buyFactory")
# mine = driver.find_element(By.ID, "buyMine")
# shipment = driver.find_element(By.ID, "buyShipment")
# alchemyLab = driver.find_element(By.ID, "buyAlchemy lab")
# portal = driver.find_element(By.ID, "buyPortal")
# timeMachine = driver.find_element(By.ID, "buyTime machine")
#
# while True:
#     money = float(driver.find_element(By.ID, "money").text)
#     time_shop = time.time() + 5
#     while time.time() < time_shop:
#         cookie.click()
#     if money >= float(timeMachine.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         timeMachine.click()
#     elif money >= float(portal.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         portal.click()
#     elif money >= float(alchemyLab.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         alchemyLab.click()
#     elif money >= float(shipment.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         shipment.click()
#     elif money >= float(mine.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         mine.click()
#     elif money >= float(factory.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         factory.click()
#     elif money >= float(grandma.text.split("\n")[0].split("-")[1].strip().replace(",","")):
#         grandma.click()
#     else:
#         cursor.click()
#     if time.time()>timeout:
#         break

