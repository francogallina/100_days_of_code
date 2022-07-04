from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)      # Extrae etiqueta+string
#print(soup.title.name)      # Extrae solo el nombre de la etiqueta
#print(soup.title.string)      # Extrae solo el string del título

#print(soup)      # Extrae el HTML
#print(soup.prettify())      # Extrae el HTML y le agrega sangrías

#print(soup.a)      # Extrae etiqueta + string del primer anclaje

"""Extraer todos los tags del archivo
si busco por class se utiliza 'class_' """
all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

"""Extraer Texto de los anchor"""
#for tag in all_anchor_tags:
    #print(tag.getText())

"""Extraer href de los anchor"""
#for tag in all_anchor_tags:
    #print(tag.get("href"))

"""Extraer solo un tag con un id"""
#heading = soup.find(name="h1", id="name")
#print(heading)

"""Select_one nos da la primera coincidencia y select todos los elementos coincidentes en una lista"""
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name") # Para buscar por ir se utiliza #nombreId
print(name)

headings = soup.select(".heading") # para las clases se utiliza el punto antes del nombre de la clase"
print(headings)

