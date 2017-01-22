import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/FordMustang"
this_page = urllib.request.urlopen(url)
soup = BeautifulSoup(this_page, "html.parser")

print(soup.title)