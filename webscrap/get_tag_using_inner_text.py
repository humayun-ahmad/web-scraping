import requests
from bs4 import BeautifulSoup

url = "https://www.nba.com/players/jalen/adams/1629824"

html = requests.get(url)

soup = BeautifulSoup(html.text,'lxml')

hight = soup.find_all('p', string='\n      HEIGHT\n    ')
print(hight)


# url = 'HEIGHT
#     '