from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.nytimes.com/topic/organization/group-of-20")
nytimes_web_page = response.text

soup = BeautifulSoup(nytimes_web_page, "html.parser")

article_titles = soup.find_all("article", class_="css-1l4spti")

for title in article_titles:
    print(article_titles)