import requests
from bs4 import BeautifulSoup

url = "https://gaana.com/"

res = requests.get(url)
print(res)
soup = BeautifulSoup(res.text, 'lxml')

for i in soup.find_all('a', href = True):
	fl = i['href']
	if fl == '':
		pass
	elif(fl[0] != 'h'):
		pass
	else:
		print(fl)

	