from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests


driver = webdriver.PhantomJS(executable_path = r"F:\Softwares\phantomJS\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")

url = "https://www.nba.com/players/steven/adams/203500"

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')


ht_doc = soup.find('section', class_ = 'nba-player-header__item nba-player-header__headshot')

img = ht_doc.find('img')


f = open('steven_adam.jpg','wb')

f.write(requests.get(img['src']).content)
f.close()
driver.quit()


