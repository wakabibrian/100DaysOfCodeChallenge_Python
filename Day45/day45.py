# Beautiful soup is a module which helps developers to pull out relevant code from HTML
# -------------Parsing HTML and Making Soup---------------------#
from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # Parsing of HTML content
# print(soup.title) # Prints whole title tag and the content
# print(soup.title.name)  # Name of the title tag
# print(soup)  # prints the entire html
# print(soup.prettify())  # prints the entire html which is indented
# print(soup.a)  # Gets the first anchor tag on the website
# print(soup.p)  # Gets the first p tag on the website
