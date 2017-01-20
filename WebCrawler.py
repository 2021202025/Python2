import requests
from bs4 import BeautifulSoup

def webcrawler(max_pages):
    page=1
    while page <= max_pages:
        url='https://thenewboston.com/forum/recent_activity.php?page=' +str(page)
        source_code = requests.get(url)
        text = source_code.txt
        Soup = BeautifulSoup(text)
        for link in Soup.findall('a', {'class': 'title text-semibold'}):
            href = "https://thenewboston.com" + link.get('href')
            print(href)

webcrawler(1)
