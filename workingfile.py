from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

root = "https://www.google.com/"
link = "https://www.google.com/search?q=bnp&source=lmns&tbm=nws&bih=929&biw=1920&hl=en&sa=X&ved=2ahUKEwi6ko-8lKv3AhVHidgFHaItAa4Q_AUoAnoECAEQAg"

req = Request(link, headers={'User-Agent': 'Mozilla/5.5'})
webpage = urlopen(req).read()
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    print(soup)