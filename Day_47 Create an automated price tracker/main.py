import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/interruptor-iluminaci%C3%B3n-retroiluminada-desmontable-anodizado/dp/B07YNHZ78Y/ref=sr_1_1_sspa?keywords=gaming+keyboard&pd_rd_r=1fafeb80-859b-446d-87bd-c8b8497a9c70&pd_rd_w=asFzE&pd_rd_wg=nrq58&pf_rd_p=8148f1e1-83ed-498f-85be-ff288b197da7&pf_rd_r=9VGFNBZAWZ8VPCBXY8B6&qid=1652404136&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRzZKRjJZVFhWRzQ2JmVuY3J5cHRlZElkPUEwMDY2NjU3MTBYM05ZT1hOSTdBOSZlbmNyeXB0ZWRBZElkPUEwODAxMTc1MlJKM0s0RzNJQTlaMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
HEADERS = {"Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
  }
response = requests.get(URL, headers=HEADERS)
print(response.content)
soup1 = BeautifulSoup(response.content, "lxml")

price_first = float(soup1.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price_first)