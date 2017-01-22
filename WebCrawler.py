import requests
from bs4 import BeautifulSoup

yellow = requests.get("http://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles%2C+CA")

text = yellow.txt
Soup = BeautifulSoup(text)
Soup.findAll("a")