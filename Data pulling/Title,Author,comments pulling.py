'''
source: 
    https://www.datacamp.com/community/tutorials/scraping-reddit-python-scrapy
'''
import requests
import urllib.request as rr
import csv
import time
from bs4 import BeautifulSoup

url = "https://old.reddit.com/r/datascience/"

#headers = {'User-Agent': 'Mozilla/5.0'}
#page = requests.get(url, headers=headers)

#page = r.get(url)
page = rr.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
domains = soup.find_all("span",class_="domain")

attrs = {'class': 'thing','data-domain': 'self.datascience'}

for post in soup.find_all('div',attrs=attrs):
    title = post.find('p',class_="title").text
    print(title)
    #print("\n\n")
    #print(post.attrs['data-domain'])

#print("\n\nThe Author\n\n")
for post in soup.find_all('div',attrs=attrs):
    author = post.find('a',class_="author").text
    print(author)
    #print("\n\n")

#print("Comments\n\n\n")
for post in soup.find_all('div',attrs=attrs):
    comment = post.find('a',class_="comments").text.split()[0]
    if comment == "comment":
    	comment = 0
    print(comment)

 #print("\n\n")

print("likes")
for post in soup.find_all('div',attrs=attrs):
    likes = post.find("div", attrs = {"class": "score likes"}).text
    if likes == ".":
    	likes = "none"
    print(likes)

counter = 1

for post in soup.find_all('div', attrs = attrs):
	title = post.find('p',class_="title").text
	author = post.find('a',class_="author").text
	comment = post.find('a',class_="comments").text.split()[0]
	if comment == "comment":
		comment = 0
	likes = post.find("div", attrs = {"class": "score likes"}).text
	if likes == ".":
		likes = "none"
	post_line = [counter, title, author, likes, comment]

	with open('output.csv','a') as f:
		writer = csv.writer(f)
		writer.writerow(post_line)
	counter += 1
	




'''
for domain in domains:
    for link in domain.find('a'):
        print(link.string)
        
    print("\n\n")

#print(domains)
'''


#print(soup.prettify())
