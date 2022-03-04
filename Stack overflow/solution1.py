# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:52:21 2022

@author: Humayun

Question-link : https://stackoverflow.com/questions/71341533/how-to-get-the-url-from-extracted-information-from-a-website
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://www.volvogroup.com/en/news-and-media/press-releases.html"
source = requests.get(url)
soup = bs(source.text , "html.parser")

news_check = soup.find_all("a" , class_ = "articlelist__contentDownloadItem")
    
data = set()

for i in news_check:
    pdf_link ="https://www.volvogroup.com"  + i['href']
    
    data.add(pdf_link)
    
    # for j in i.find_all('href'):
    #     pdf_link = + j.get('.pdf')
    #     data.add(j)
    #     print(pdf_link)
    
df = pd.DataFrame(data)
print(df)