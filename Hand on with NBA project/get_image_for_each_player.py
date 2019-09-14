from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
from urllib.request import urlretrieve as p
import random

driver = webdriver.PhantomJS(executable_path = r"F:\Softwares\phantomJS\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")

url = "https://www.nba.com/players/steven/adams/203500"

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')


ht_doc = soup.find('section', class_ = 'nba-player-header__item nba-player-header__headshot')

img = ht_doc.find('img')

link = img['src']
test = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/203500.png'
f = open("xxxxx.jpg", "wb")
f.write(requests.get(test).content)
f.close()
driver.quit()


#print(img['src'])
