# Beautiful soup helps us to pull out relevant code from HTML
# -------------Parsing HTML and Making Soup---------------------#
from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
print(soup.a)  # The first anchor tag in the website
print(soup.li)  # The first li tag in the website
print(soup.p)  # The first p tag in the website
