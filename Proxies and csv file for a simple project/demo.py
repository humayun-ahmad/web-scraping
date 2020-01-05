from bs4 import BeautifulSoup
import requests

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxyDict = { 
    "http"  : http_proxy, 
    "https" : https_proxy, 
    "ftp"   : ftp_proxy
}

url = 'https://www.bestreviews.guide/categories'

def hunt_title():
	header =  {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}

	res = requests.get(url,headers=header)
	soup = BeautifulSoup(res.text,'lxml')

	# all categories_link link here:
	categories_link = soup.find_all('a', class_='main_categories__title__container')

	# one by one categories_link browes here:
	for one in categories_link:
		main_link = 'https://www.bestreviews.guide'
		full_categories_link = main_link + one['href']

		after_categories_res = requests.get(full_categories_link,headers=header)
		after_categories_soup = BeautifulSoup(after_categories_res.text,'lxml')

		# all sub_categories_link link here:
		sub_categories_link = after_categories_soup.find_all('a',class_='gray_box_layout')

		# print(sub_categories_link)

		# each_sub_categories link browes here:
		for sub_one in sub_categories_link:
			full_sub_categories_link = main_link + sub_one['href']
			
			each_product_res = requests.get(full_sub_categories_link,headers=header)
			each_product_soup = BeautifulSoup(each_product_res.text,'lxml')

			# find title_container tag here:
			title_container = each_product_soup.find_all('div',class_='gray_box_layout--txt')

			# for loop print the title from title_container:
			for title in title_container:

				print(title.text.strip())

				break

			# print(title)
			
			break

		break

		# after_categories

		# print(full_categories_link)	

	# print(categories_link)


if __name__ == '__main__':
	hunt_title()

