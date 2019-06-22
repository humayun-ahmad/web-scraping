#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


from urllib.request import urlopen
from bs4 import BeautifulSoup as b


# In[27]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)


# In[28]:


soup = b(html,'html.parser')
#soup = b(html,'lxml')
type(soup)


# In[31]:


# get the title
title = soup.title
print(title)


# In[30]:


#print out the text
print(soup.prettify())


# In[62]:


#print out the text
text = soup.get_text()
print(text)


# In[63]:


for links in soup.find_all('a'):
    print(links)
    #link = links.get('href')
    #print(link)


# In[67]:


#print the first 10 rows for sanity check
#rows = soup.find_all('tr')
rows = soup.find_all('tr')
print(rows)


# In[84]:


for row in rows:
    row_td = row.find_all('td')
print(row_td)    
print("\n\n\n")
print(type(row_td))

for row_td1 in row_td:
    print(row_td1.text)


# In[93]:


str_cells = str(row_td)
print(str_cells)
print("\n\n\n")
cleantext = b(str_cells,"html.parser").get_text()
print(cleantext)
type(cleantext)


# In[94]:


import re
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean,'',str_cells))
    list_rows.append(clean2)

print(clean2)
type(clean2)


# In[95]:


df = pd.DataFrame(list_rows)
df.head(10)


# In[96]:


df1 = df[0].str.split(',',expand=True)
df1.head(10)


# In[97]:


df1[0] = df1[0].str.strip('[')
df1.head(10)


# In[98]:


col_labels = soup.find_all('th')


# In[99]:


all_header = []
col_str = str(col_labels)
cleantext2 = b(col_str,"lxml").get_text()
all_header.append(cleantext2)
print(all_header)


# In[100]:


df2 = pd.DataFrame(all_header)
df2.head()


# In[103]:


df3 = df2[0].str.split(',',expand=True)
df3.head()


# In[104]:


frames = [df3,df1]
df4 = pd.concat(frames)
df4.head(10)


# In[106]:


df5 = df4.rename(columns = df4.iloc[0])
df5.head(10)


# In[ ]:




