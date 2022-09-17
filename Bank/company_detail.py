# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:27:31 2022

@author: Rajib
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pathlib,pickle
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Github credentials
email = "" # Enter your email address
password = "" # Enter your password

# initialize the Chrome driver
driver = webdriver.Chrome()


login_path = "https://finbox.com/login/email" # login route


""" For getting the sessionID and Cookies """
def save_cookies_file(): 
    driver.get(login_path)
    
    # login info
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    
    # submit button
    driver.find_element(By.CLASS_NAME, '_105e3d41').click()
    
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    time.sleep(10)

save_cookies_file();


final_data = []


""" Previous Cookies are being used here and this function will take the name of bank and will return the whole information this is only for income sheet and same function will work for Balance sheet and cash flow Statement as well. """
def search(text):    
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    bank_path = f"https://finbox.com/DSE:{text}"
    full_path = bank_path + "/financials/income_statement"
    
    driver.get(full_path)
    soup = bs(driver.page_source, "html.parser")
    table = soup.find("div", {'class' : "rt-tbody"}).find_all('div', {'class' : "rt-tr-group"})
    # table 
    table_header = soup.find("div", {'class' : "rt-tr"})
    # print(table_header)
    
    t_head = [] # it will hold table header data
    
    for th in table_header:
        #print(th.get_text())
        t_head.append(th.get_text())
 
    
    result = [] # this list will hold main data
    header = [] # table left_side_header
    for item in table:
        # print(item.get_text())
        
        try:
            # print(item.get_text())
            for i in item:
                check = 0
                for j in i:
                    if check == 0:
                        check = 1
                        res1 = j.get_text() # + " "
                        header.append(res1)
                    else:
                        res = j.get_text() # + " "
                        # print(res)
                        result.append(res)
                
        except:
            print("Something is going wrong")
        
    
    # for x in header:
    #     print(x)
    
    
    time.sleep(10)
    

search("DHAKABANK") # this is main function, here you have to put the value of trading code.


time.sleep(10)
driver.close()










