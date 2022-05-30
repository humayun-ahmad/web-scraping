# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:44:09 2022

@author: acer
"""

'''
import json

with open('scores.json') as f:
    jsonData = json.load(f)
    

turnament = jsonData['events'][0]['tournament']['name']
homeTeam = jsonData['events'][0]['homeTeam']['name']
awayTeam = jsonData['events'][0]['awayTeam']['name']

homeScore = jsonData['events'][0]['homeScore']
awayScore = jsonData['events'][0]['awayScore']

print(homeScore,"\n", awayScore)

print(turnament,"\n", homeTeam,"\n", awayTeam)
'''

str1 = "aaaabbsaa"
k = list(str1)
dict1 = {}
for char in k:
    cnt = 0
    for i in range(len(k)):
        if char == k[i]:
            cnt=cnt+1
    dict1[char] = cnt 

for i in dict1:
    print(i,dict1[i])

