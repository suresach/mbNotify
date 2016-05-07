from urllib.request import urlopen
from bs4 import BeautifulSoup
code_box = urlopen('http://www.infibeam.com/deal-of-the-day.html').read()
mydivs = soup.find("div", { "class" : "carousel_list" })
lins = mydivs.find_all('a')
for links in lins:
    print(links.get_text(), end = '')
