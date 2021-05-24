import requests
from bs4 import BeautifulSoup

def spider():
    url = 'http://news.ceic.ac.cn/index.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    res = requests.get(url, headers)
    with open("earth.html", "w", encoding="utf-8") as fp:
        fp.write(res.content.decode("utf-8"))
    # print(res.content.decode("utf-8"))
