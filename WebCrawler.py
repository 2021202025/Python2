import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/FordMustang"
this_page = urllib.request.urlopen(url)
soup = BeautifulSoup(this_page, "html.parser")

print(soup.title.text)

for link in (soup.findAll('a')):
    print(link.get('href'))
    print(link.text)