from bs4 import BeautifulSoup
html = "<div>Hello<p>this is a test</p></div>"
soup = BeautifulSoup(html, 'html.parser')
for p in soup.find('p'):
    p.extract()
print(soup)