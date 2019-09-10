from selenium import webdriver
from bs4 import BeautifulSoup
import re

#f = open("sample_file.txt",'a+')

driver = webdriver.PhantomJS(executable_path=r'F:\Softwares\phantomJS\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
t = 0
while t < 1:
	t = t + 1
	url = "https://www.nba.com/players"
	driver.get(url)

	

	ht_doc = BeautifulSoup(driver.page_source, 'lxml')

	test_link = ht_doc.find_all('a',class_ = 'row playerList')
	for ln in test_link:
		string1 ="www.nba.com" + ln.get('href')
		#print(string1)

		driver.get(string1)

		each_players_html = BeautifulSoup(driver.page_source,'lxml')

		#print(each_players_html)

		a_section = each_players_html.find('section', class_='nba-player-vitals small-12 large-6')


		print(a_section)

		#Height = each_players_html.findNextSiblings('p')

		break




	# for a in ht_doc.find('a'):
	# 	link = a.get('href')
	# 	link = "www.nba.com" + link
	# 	driver.get(link)

	# 	code = driver.page_source

	# 	# print(code)

	# 	soup = BeautifulSoup(code,'lxml')
	# 	print(soup.prettify())

	# 	Height =""

	# 	all_section = soup.find('section', class_ = "nba-player-vitals small-12 large-6")
		#print(all_section)
		#st = all_section.find('section', class_ = 'nba-player-vitals__top-left small-6')
		# output = ""
		# for out in st.find_all('p'):
		# 	output = output + str(out.text)
		# 	output = re.sub(' +', ' ',output)
		# 	output = output.replace("\n", " ")
		# 	output = re.sub(' +', ' ',output)
			#f.write(output + "\n")

		#f.close()



#print(all_section)







