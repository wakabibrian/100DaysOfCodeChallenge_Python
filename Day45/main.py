import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

# titles = [title.getText().split()
#           for title in soup.find_all(name="h3", class_="title")]
# title_texts = [title.pop(0) for title in titles]
# final_title = [title_text for title_text in title_texts]

titles = soup.find_all(name="h3", class_="title")

movies = [title.getText()
          for title in soup.find_all(name="h3", class_="title")]

movies.reverse()


with open("movies.txt", "w", encoding="ISO-8859-1") as new_file:
    for movie in movies:
        new_file.write(f"{movie}\n")
