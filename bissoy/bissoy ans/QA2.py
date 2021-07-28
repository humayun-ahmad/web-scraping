# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 02:06:32 2020

@author: acer
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# driver = webdriver.PhantomJS(executable_path=r'C:\webdriver\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# res = BeautifulSoup(driver.page_source, 'lxml')

url = "https://www.bissoy.com/q/1111111262187"


print(url.split('/')[-1])