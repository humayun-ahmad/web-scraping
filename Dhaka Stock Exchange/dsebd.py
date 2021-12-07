from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
url = "https://www.dsebd.org/latest_share_price_scroll_l.php"

driver = webdriver.Firefox(executable_path=r"C:/webdriver/geckodriver-v0.26.0-win64/geckodriver.exe")
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)
table = soup.find_all('table', {'class': 'table table-bordered background-white shares-table fixedHeader'})

df = pd.read_html(str(table))

print(df)

