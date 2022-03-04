# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:52:21 2022

@author: Humayun

Question-link : https://stackoverflow.com/questions/71341533/how-to-get-the-url-from-extracted-information-from-a-website
"""
import requests
import pprint
from bs4 import BeautifulSoup as bs


req = requests.get('https://api.randomtube.xyz/video.get?chan=2ch.hk&board=b&page=1')

soup = req.json()

datas = soup['response']['items']

for data in datas:
    print(data['url'])