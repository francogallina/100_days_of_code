import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
with open ("list_film.txt", "w") as lf:


    web = requests.get(URL).text
    soup = BeautifulSoup(web, "html.parser")

    titles = soup.find_all(name="h3", class_="title")
    title_list = [t.getText() for t in titles]

    new_title_list = list(reversed(title_list))
    for i in new_title_list:
        lf.write(i + "\n")

