import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.nba.com/')
soup = BeautifulSoup(res.text, 'lxml')
h1 = soup.select("title")

print(h1[0].getText())
