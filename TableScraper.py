import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

soup = make_soup("http://www.basketball-reference.com/players/a/")

playerdatasaved = " "
for record in soup.findAll('tr'):
    playerdata = ""
    for data in record.findAll('td'):
        playerdata = playerdata+","+data.text
    playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "Player,From,To,Pos,Ht,Wt,Birth Date,College" + "\n"
file = open(os.path.expanduser("Basketball.csv"),"wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))

