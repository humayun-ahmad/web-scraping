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
    print("\n\n")
    #print(post.attrs['data-domain'])

print("\n\nThe Author\n\n")
for post in soup.find_all('div',attrs=attrs):
    author = post.find('a',class_="author").text
    print("Author = ", author)
    print("\n\n")

print("Comments\n\n\n")
for post in soup.find_all('div',attrs=attrs):
    comment = post.find('a',class_="comments").text
    print(comment)
    print("\n\n")


'''
for domain in domains:
    for link in domain.find('a'):
        print(link.string)
        
    print("\n\n")

#print(domains)
'''


#print(soup.prettify())
