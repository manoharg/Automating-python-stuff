#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:00:13 2017

@author: manohar
"""

import requests
res=requests.get("http://www.google.com")
try:
    res.raise_for_status()
except:
    print("Error in downloading")
file=open("google.html","wb")
for chunck in res.iter_content(100000):
    file.write(chunck)
file.close()