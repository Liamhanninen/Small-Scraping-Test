# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:42:30 2015

@author: liamh
"""

import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import requests


url = 'http://post-gazette.com/local/breaking.more'
r = requests.get(url)
content = r.text
soup = BeautifulSoup(content)
linesoup = soup.find_all("div", class_="innertube10 hundred")
stringsoup = str(linesoup)
#The above lines grab/get url, parse it, and then turn it into a 
#string so Python can do its thing


with open ("scrapecrimedata3" + ".txt", "w+") as newfile:
    newfile.write(stringsoup)
#The above lines create (if not created already) and write the 
#parsed html to a .txt file


def filtered():
    with open ("scrapecrimedata3" + ".txt", "r") as newfile:     
        with open("filtered" + ".txt", "a") as filtered:
            for line in newfile:
                if "police" in line: filtered.write(line)
()
'''
The above lines search that .txt file for a specific keyword
and then add any lines with those keywords to a new .txt file
This is what I am trying to fix/improve;
    I can only seem to search for a single keyword. In this case
    "police" is the only string I can search for. Separating by
    commas and/or using 'and' and 'or' did not seem to work.
    '''
       
filtered()       

#htmlgrab
#write

