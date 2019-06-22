import requests as rr
import urllib.request as r
from bs4 import BeautifulSoup as b

url ="https://www.thecrazyprogrammer.com/"


    
data = r.urlopen(url)
#data=requests.get(url)
#print(r)
soup = b(data,"html.parser")
#print(soup.title.string)
#print(soup.prettify())
for links in soup.find_all('a'):
    link = links.get('href')
    if link=="#main" or link == "#":
        print("https://www.thecrazyprogrammer.com/")
    else:
        print(link)
       
