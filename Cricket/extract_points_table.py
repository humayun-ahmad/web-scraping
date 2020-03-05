from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

page = requests.get("http://www.cricbuzz.com/cricket-series/2678/india-and-bangladesh-in-sri-lanka-t20i-tri-series-2018/points-table")

soup = BeautifulSoup(page.text)
# print(soup.prettify())

scoretable = soup.find('table', class_="table cb-srs-pnts")

team_name = [tn.get_text() for tn in scoretable.find_all('td', class_="cb-srs-pnts-name")]

table_head = [th.get_text() for th in scoretable.find_all('td', class_="cb-srs-pnts-th")]

table_head.insert(5,'pts')
# print(table_head)

scores = [td.get_text() for td in scoretable.find_all('td', class_="cb-srs-pnts-td")]
teams_point = np.array(scores)
teams_point = teams_point.reshape(3,7)
# print(teams_point)

df = pd.DataFrame([teams_point[0][:], teams_point[1][:], teams_point[2][:]],index=team_name,columns=table_head)
#print(df)


