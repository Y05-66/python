import requests
from bs4 import BeautifulSoup
import time

for page in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={page}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/136.0.0.0''Safari/537.36 Edg/136.0.0.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    all_movies = soup.findAll("div", class_="item")

    for movie in all_movies:
        title = movie.find("span", class_="title")
        rating = movie.find("span", class_="rating_num")
        quote_tag = movie.find("span", class_="ing")
        quote = quote_tag if quote_tag else "无"

    with open("douban_movies.json", "a", encoding="utf-8") as fp:
        fp.write(f"{title} | 评分：{rating} | 引言：{quote}\n")