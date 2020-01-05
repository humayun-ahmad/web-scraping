import requests
from bs4 import BeautifulSoup

session = requests.session()
form_page = session.get('http://www.educationboardresults.gov.bd')
form = BeautifulSoup(form_page.content, 'lxml')

captcha = eval(form.form.table.table.find_all('tr')[6].find_all('td')[1].get_text())
data = dict(sr=3,et=0,exam='jsc', year='2019', board="dhaka", roll="399284", reg="1910345555", value_s=captcha)
result_page = session.post('http://www.educationboardresults.gov.bd/result.php', data=data)
result = BeautifulSoup(result_page.content, 'lxml')