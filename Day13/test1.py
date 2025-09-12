from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
image = bsObj.findAll("img", {"src": re.compile(r"\.\./img/gifts/img.*\.(jpg|jpeg|png|gif)")})
for img in image:
    print(img["src"])