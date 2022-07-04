from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")




""" Obtener la primer ocurrencia """



"""
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link= article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)
"""



""" Obtener todas las ocurrencias """



article = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for tag in article:
    text = tag.getText()
    link = tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_= "score")]

# print(article_texts)
# print(article_links)
#print(article_upvotes)


"""Obtener el título y link del artículo con más votos - 2 maneras"""

#1
"""
max = 0
count = 0
for i in article_upvotes:
    count=+1
    if i>max:
        max=i

print(article_texts[count])
print(article_links[count])
print(article_upvotes[count])

"""

#2

largest_upvote = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvote)
print(article_texts[largest_index])
print(article_links[largest_index])