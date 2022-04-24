from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

root = "https://www.google.com/"
link = "https://www.google.com/search?q=biden&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwjAvsKDyOXtAhXBhOAKHXWdDgcQpwUIKQ&biw=1604&bih=760&dpr=1.2"

req = Request(link, headers={'User-Agent': 'Mozilla/5.5'})
webpage = urlopen(req).read()
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    print(soup)
    for item in soup.find_all('div', attrs={'class': 'KCrYT'}):
        print(item)