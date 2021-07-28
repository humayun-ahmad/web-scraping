# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:46:57 2020

@author: acer
"""


from bs4 import BeautifulSoup
import requests
import time

url = "https://www.bissoy.com/topic/%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A7%8D%E0%A6%AF+%E0%A6%93+%E0%A6%9A%E0%A6%BF%E0%A6%95%E0%A6%BF%E0%A7%8E%E0%A6%B8%E0%A6%BE"

# response =requests.get(url)

# # print(response.status_code)

# soup = BeautifulSoup(response.text, 'lxml');

# question_body = soup.find_all('div', class_='ofr-n card')

question_link = []

# for body in question_body:
#     q_link=body.find('a', style="text-decoration:none;color:inherit").get('href')
#     # print(q_link)
#     question_link.append(q_link)
 
page = 1
error_link_address = open("error_link.txt", "w")
output = open("output.txt", 'w')

while(page<=826):
    # url = "https://www.bissoy.com/topic/%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A7%8D%E0%A6%AF+%E0%A6%93+%E0%A6%9A%E0%A6%BF%E0%A6%95%E0%A6%BF%E0%A7%8E%E0%A6%B8%E0%A6%BE"

    response =requests.get(url)
    
    # print(response.status_code)
    
    if(response.status_code==200):
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        question_body = soup.find_all('div', class_='ofr-n card')
        
        for body in question_body:
            q_link=body.find('a', style="text-decoration:none;color:inherit").get('href')
            # print(q_link)
            # question_link.append(q_link)
            output.write(q_link+'\n')
            
        page = page+1
        url = "https://www.bissoy.com/topic/%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A7%8D%E0%A6%AF+%E0%A6%93+%E0%A6%9A%E0%A6%BF%E0%A6%95%E0%A6%BF%E0%A7%8E%E0%A6%B8%E0%A6%BE"+"?page="+ str(page)
        
    else:
        error_link_address.write(url)
    # break
    time.sleep(3)
    
# print(question_link)

error_link_address.close()

output.close()




# print(question_body)