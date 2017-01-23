import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

soup = make_soup("http://www.basketball-reference.com/players/a/")

for record in soup.findAll('tr'):
    print(record.text)
