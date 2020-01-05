from bs4 import BeautifulSoup
from requests import *
import csv

f = open('English_2018.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(f)

def linkmine():
    #minelink = []
    for i in range(3):
        main_url = 'https://www.discogs.com'
        url = 'https://www.discogs.com/search/?q=&country_exact=US&year=2016&type=all&page={0}'.format(
            i)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
        res = get(url,headers = header)
        soup = BeautifulSoup(res.content, 'html.parser')

        for linksource in soup.find_all("div",{"class":"cards cards_layout_large"}):
            all_link = linksource.find_all("a",class_="search_result_title")
            for links in all_link:
                link = links.get('href')
            print(all_link)

if __name__ == '__main__':
    linkmine()