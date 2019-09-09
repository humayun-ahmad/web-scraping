# row players-wrapper

from selenium import webdriver
from bs4 import BeautifulSoup

#create driver
f = open("Player_Name_and_Link.txt","w+")

class Player():
	def _init_(self):
		self.name = ""
		self.link = ""




driver = webdriver.PhantomJS(executable_path = r'F:\Softwares\phantomJS\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = "https://www.nba.com/players"
driver.get(url)

#download html page

#print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'lxml')

div = soup.find('div',class_='row players-wrapper')
#print(div)
t=0
Player_list = []

for a in div.find_all('a'):
	b = a.find('span')
	new_Play = Player()
	new_Play.name = b.text
	new_Play.link = "www.nba.com" + a['href']
	Player_list.append(new_Play)

for one_Player in Player_list:
	t = t + 1
	f.write(str(t)+". " + str(one_Player.name)+" " + str(one_Player.link)+"\n")

	#print (one_Player.name)
	#print (one_Player.link)
	#print("www.naba.com" + a['href'])
	
	#t = t + 1 
	#f.write(str(t) + ". " +str(b.text) + "\n")
	#print(b.text)

f.close()
driver.quit()






