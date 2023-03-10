from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/animation/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="b-content__inline_item")
    animes = []
    for item in items:
        info = item.find('div', class_="b-content__inline_item-link").find('div').string.split(', ')
        anime = {
            'title': item.find('div', class_="b-content__inline_item-link").find('a').string,
            'link': item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            'date': info[0],
            'country': info[1],
            'genre': info[2],
            'status': item.find('span', class_="info").string
            if item.find('span', class_="info") is not None else "Полнометражка"
        }
        animes.append(anime)
    return animes


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animes = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            anime = get_data(html.text)
            animes.extend(anime)

        return animes
    else:
        raise Exception("Error in parser!")

