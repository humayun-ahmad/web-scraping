#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[61]:


from urllib.request import urlopen
from bs4 import BeautifulSoup as b


# In[62]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)


# In[63]:


soup = b(html,'html.parser')
#soup = b(html,'lxml')
type(soup)


# In[64]:


# get the title
title = soup.title
print(title)


# In[65]:


#print out the text
print(soup.prettify())


# In[66]:


#print out the text
text = soup.get_text()
print(text)


# In[67]:


for links in soup.find_all('a'):
    print(links)
    #link = links.get('href')
    #print(link)


# In[68]:


#print the first 10 rows for sanity check
#rows = soup.find_all('tr')
rows = soup.find_all('tr')
print(rows)


# In[69]:


for row in rows:
    row_td = row.find_all('td')
print(row_td)    
print("\n\n\n")
print(type(row_td))

for row_td1 in row_td:
    print(row_td1.text)


# In[70]:


str_cells = str(row_td)
print(str_cells)
print("\n\n\n")
cleantext = b(str_cells,"html.parser").get_text()
print(cleantext)
type(cleantext)


# In[71]:


import re
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean,'',str_cells))
    list_rows.append(clean2)
print(list_rows)
print(clean2)
type(clean2)


# In[72]:


df = pd.DataFrame(list_rows)
df.head(10)


# In[89]:


df1 = df[0].str.split(',',expand=True)
df1.head(10)


# In[91]:


df1[0] = df1[0].str.strip('[')
df1[13] = df1[13].str.strip(']')
df1.head(10)


# In[92]:


col_labels = soup.find_all('th')
print(col_labels)


# In[93]:


all_header = []
col_str = str(col_labels)
cleantext2 = b(col_str,"lxml").get_text()
all_header.append(cleantext2)
print(all_header)
print(cleantext2)


# In[94]:


df2 = pd.DataFrame(all_header)
df2.head()


# In[95]:


df3 = df2[0].str.split(',',expand=True)
df3.head()


# In[96]:


frames = [df3,df1]
df4 = pd.concat(frames)
df4.head(10)


# In[97]:


df5 = df4.rename(columns = df4.iloc[0])
df5.head(10)


# In[98]:


df5.info()
df5.shape


# In[99]:


df6 = df5.dropna(axis=0,how='any')
df6.head(10)


# In[100]:


df7 = df6.drop(df6.index[0])
df7.head(10)


# In[112]:


df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team': 'Team'},inplace=True)
df7.head(10)


# In[124]:


time_list = df7[' Chip Time'].tolist()
#print(time_list)

#you can use a for loop to convert Chip Time minutes

time_mins = []
for i in time_list:
    #print(type(i))
    h = 0
    if i.count(':') == 1:
        m,s=i.split(':')
    else:
        h,m,s = i.split(':')
    #print(h,m,s)
    math = (int(h) * 3600 + int(m) * 60 + int(s) ) / 60
    time_mins.append(math)
print(time_mins)


# In[126]:


df7['Runner_mins'] = time_mins
df7.head(10)


# In[129]:


df7.describe(include=[np.number])
#df7.describe(include='all')


# In[131]:


df7.describe()


# In[ ]:




