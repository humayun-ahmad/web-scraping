from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.bestreviews.guide/categories'

header =  {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}

# for main categories title list:
main_categories_name = []
# for sub categories title list:
sub_categories_name = []


# main url get requests here:
res = requests.get(url,headers=header)
soup = BeautifulSoup(res.text,'lxml')

# all categories_link link here:
categories_link = soup.find_all('a', class_='main_categories__title__container')

# all categories title here:
main_categories__title = soup.find_all('h3' , class_='main_categories__title')

# print(main_categories__title)

# text file create and append here:
f = open('title.txt','a')

def call():
    # all main_categories__title stay in the list:
    for one_title in main_categories__title:
        one_title_string = one_title.text.lstrip().rstrip()
        main_categories_name.append(one_title_string)


    # main_categories_name write in csv file:
    '''
    with open('sample1.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(main_categories_name)
    ''' 

    #    

    # one by one categories_link browes here:
    for one in categories_link:
        main_link = 'https://www.bestreviews.guide'
        full_categories_link = main_link + one['href']
    #     print(two.text)
        after_categories_res = requests.get(full_categories_link,headers=header)
        after_categories_soup = BeautifulSoup(after_categories_res.text,'lxml')

        # all sub_categories_link link here:
        sub_categories_link = after_categories_soup.find_all('a',class_='gray_box_layout')
        
        for one_sub in sub_categories_link:
        	sub_categories_name.append(one_sub.text)
        # print(sub_categories_link)

        # each_sub_categories link browes here:
        for sub_one in sub_categories_link:
            full_sub_categories_link = main_link + sub_one['href']

            each_product_res = requests.get(full_sub_categories_link,headers=header)
            each_product_soup = BeautifulSoup(each_product_res.text,'lxml')

            # find title_container tag here:
            title_container = each_product_soup.find_all('div',class_='gray_box_layout--txt')

            # when start the sub categories print @ sign:
            f.write("@")

            # for loop print the title from title_container:
            for title in title_container:

                # print(title.text.strip().lstrip().rstrip())

                st = title.text.strip().lstrip().rstrip() + ','

                f.write(st)
                

                # break

            # print(title)

            # break

        # break

        # after_categories

    # print(categories_link)


    f.close()


if __name__ == '__main__':
    call()
