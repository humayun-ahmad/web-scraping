import requests
from bs4 import BeautifulSoup as bs

header =  {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}

list = []
url_file = open("linkfile.txt", "r") 
# file = open("output.txt","w")

for url in url_file:
    response = requests.Session()
    response = response.get(url, headers=header)
    soup = bs(response.text, 'lxml')
    t = soup.find('span', class_='a-size-large', id="productTitle")
    if t == '':
        continue
    else:
        list.append(t.text)

file = open("output.txt", "w")
for title in list:
    file.write(title.strip() + "\n")
file.close()