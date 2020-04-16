```
#link:  https://stackoverflow.com/questions/27195569/how-to-get-text-from-within-a-tag-but-ignore-other-child-tags
# how to ignore a tag 
```
from bs4 import BeautifulSoup
html = "<div>Hello<p>this is a test</p></div>"

soup = BeautifulSoup(html, 'html.parser')
for div in soup.find_all('div'):
    print(div.find(text=True, recursive=False))
    