# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:42:30 2015

@author: liamh
"""

import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import requests

#def htmlgrab():
url = 'http://post-gazette.com/local/breaking.more'
r = requests.get(url)
content = r.text
soup = BeautifulSoup(content)
linesoup = soup.find_all("div", class_="innertube10 hundred")
stringsoup = str(linesoup)


#def write():
with open ("scrapecrimedata3" + ".txt", "w+") as newfile:
    newfile.write(stringsoup)


def filtered():
    with open ("scrapecrimedata3" + ".txt", "r") as newfile:     
        with open("filtered" + ".txt", "a") as filtered:
            for line in newfile:
                if "police" in line: filtered.write(line)
()
       
filtered()       

#htmlgrab
#write

