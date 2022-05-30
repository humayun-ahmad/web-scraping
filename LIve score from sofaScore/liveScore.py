# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:41:18 2022

@author: Humayun
"""

import http.client

conn = http.client.HTTPSConnection("api.sofascore.com")

payload = ""

headers = {
    'authority': "api.sofascore.com",
    'accept': "*/*",
    'accept-language': "en-US,en;q=0.9,bn;q=0.8,ru;q=0.7,hi;q=0.6",
    'cache-control': "no-cache",
    'origin': "https://www.sofascore.com",
    'pragma': "no-cache",
    'referer': "https://www.sofascore.com/",
    'sec-ch-ua': "^\^"
    }

conn.request("GET", "/api/v1/sport/football/events/live", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))