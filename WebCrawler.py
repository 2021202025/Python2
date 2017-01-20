import requests
from bs4 import beautifulsoup

def webcrawler(max_pages):
    page=1
    while page <= max_pages:
        url='https://thenewboston.com/forum/recent_activity.php?page='+str(page)
        source_code=requests.get(url)
        