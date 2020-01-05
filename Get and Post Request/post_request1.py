# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:18:24 2019

@author: Humayun Ahmad Rajib
"""

import requests
from bs4 import BeautifulSoup


#r = requests.get('https://xkcd.com/353/')
payload ={'username':'corey', 'password':'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()

print(r_dict['form'])
#print(r.text)
#print(r.json())0



