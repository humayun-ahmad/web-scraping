from googlesearch import search

query = "python scraping"

for i in search(query,tld = "com", lang="en", num = 10, start = 0, stop = 10,pause = 2):
	print(i)
