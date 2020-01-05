import requests
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.PhantomJS(executable_path=r'F:\Softwares\phantomJS\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')



def get_amazomoton_product(keyword):
	amazon = "https://www.amazon.com/"
	url = amazon+"/s?k="+keyword+"&rh=p_72:2661618011,p_n_condition-type:6461716011&s=relevanceblender&page=1&currency=USD&ref=sr_st_review-rank,sr_pg_1" 
	driver.get(url)

	ht_doc = BeautifulSoup(driver.page_source, 'lxml')
	print(ht_doc)

	


if __name__ == '__main__':
	get_amazomoton_product("phone")
