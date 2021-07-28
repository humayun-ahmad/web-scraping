# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:13:39 2020

@author: acer
"""

# =============================================================================
# # question title
# h1.card-title
# 
# # question description
# div.q_desc card-text    
# 
# # answer description
# div.answer-body mt-1 card-text
# =============================================================================

from bs4 import BeautifulSoup
import requests
import time

link_files = open('input.txt', 'r')
# error_link_file = open('error_link_file.txt', 'w')
# result = []


for link in link_files:
    print(link)
    response =requests.get(link)
    qa_number = link.split('/')[-1].strip()
    soup = BeautifulSoup(response.text, 'lxml')
    
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'lxml')
        # q_title = soup.find("h1")
        # print(q_title.text)
        # q_description = soup.select(".q-details")
        # print(q_description)
        # q_who = soup.select_one(".qa-who span").text
        # print(q_who)
        data_aid = soup.getAttribut("data-aid")
        print(data_aid['data-aid'])
        ## q_class= "#a-"+str(qa_number)
        # a_who = 
        # q_answer = soup.select("#a-1111111262187 p").text
        # print(q_answer)
        
#         print(q_title)
#         print(q_description)
#         print(q_answer)
        
#     else:
#         error_link_file.write(url)        
    break

# link_files.close()        
# error_link_file.close()

