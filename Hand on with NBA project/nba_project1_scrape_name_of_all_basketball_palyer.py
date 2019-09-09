# row players-wrapper

from selenium import webdriver
from bs4 import BeautifulSoup

#create driver
f = open("test.txt","w+")


driver = webdriver.PhantomJS(executable_path = r'F:\Softwares\phantomJS\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = "https://www.nba.com/players"
driver.get(url)

#download html page

#print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'lxml')

div = soup.find('div',class_='row players-wrapper')
#print(div)
t=0


for a in div.find_all('a'):
	b = a.find('span')
	
	t = t + 1 
	#print(b.text)
	f.write(str(t) + ". " +str(b.text) + "\n")

f.close()
driver.quit()






