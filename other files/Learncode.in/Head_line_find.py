import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
all_headline = soup.select(".mw-headline")

for i in all_headline:
	print(i.text) #this line will work 
	# print(i.getText()) # this line also work properly as same as before line 

# print(all_headline)