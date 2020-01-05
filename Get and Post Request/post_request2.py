import requests
from bs4 import BeautifulSoup

import re



url = 'http://bugs.python.org'

data = {'number': 38479,'type':'issue', 'action': 'show'}

r = requests.post(url,data = data)

# print(r.status_code)
soup = BeautifulSoup(r.text,'lxml')


print(soup)

