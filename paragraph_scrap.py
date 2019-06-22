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
for para in soup.find_all('p'):
       print(para.text)
       
