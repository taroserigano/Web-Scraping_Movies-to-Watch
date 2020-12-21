import re

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", attrs={"class": "title"})
print(all_movies)
movie_titles=[movie.getText() for movie in all_movies]

movies = movie_titles[::-1]

with open("movies.text",mode="w", encoding='utf8') as f:
    for movie in movies:
        f.write(f"{movie}\n")
