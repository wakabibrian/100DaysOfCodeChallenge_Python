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

# finding all the elements e.g p, a etc in list form
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# company_url = soup.select(selector="p a")  # The all the matching items in the list
company_url = soup.select_one(selector="p a")  # The first matching item
print(company_url)

author_name = soup.select_one(selector="#name")
print(author_name)

heading = soup.select_one(selector=".heading")
print(heading)
