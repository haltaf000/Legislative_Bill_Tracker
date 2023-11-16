import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
ny_times_webpage = response.text

soup = BeautifulSoup(ny_times_webpage, "html.parser")
article_tag = soup.find_all(name="h3", class_="title")

for article in article_tag:
    article_text = article.getText()
    print(article_text)
    