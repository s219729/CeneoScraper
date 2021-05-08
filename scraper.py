import requests
from bs4 import BeautifulSoup

respons = requests.get('https://www.ceneo.pl/63419968#tab=reviews')

page_dom = BeautifulSoup(respons.text, "html.parser")

opinions = page_dom.select("div.js_product-review")

#print(type(opinions))

opinion = opinions.pop(0)

#print(type(opinion))

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").text.strip()
recomm = opinion.select_one("span.user-post__author-recomendation").text.strip()
stars = opinion.select_one("span.user-post__score-count")
#print(type(author))
print(author)

#print(page_dom.prettify())


