from bs4 import BeautifulSoup
import requests
from form import rellenar_formulario

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22users" \
             "SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122." \
             "30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22is" \
             "MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22" \
             "value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
             "cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%" \
             "22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%" \
             "22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%" \
             "7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
HEADERS = {"Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
  }

CHROME_DRIVER_PATH = "C:\\Users\\Usuario\\Development\\chromedriver.exe"

response = requests.get(ZILLOW_URL, headers=HEADERS)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")


links = soup.find_all(name="a", class_="list-card-link")
list_link = []
for j in links:
    link = j.get("href")
    if link.split("//")[0] == "https:":
        pass
    else:
        link = "https://www.zillow.com"+link
    if link not in list_link:
        list_link.append(link)


prices = soup.find_all(name="div", class_="list-card-price")
list_price = []
for i in prices:
    p = i.getText().split("/")[0].split("$")[1].split("+")[0].replace(",", "")
    list_price.append(p)

address = soup.find_all(name="address", class_= "list-card-addr")
list_address = []
for i in address:
    list_address.append(i.getText())

dictionary = {}

bot = rellenar_formulario(CHROME_DRIVER_PATH)
for z in zip(list_address, list_price, list_link):
    bot.rellenar(z[0],z[1],z[2])







