# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from lxml import html
import requests
from bs4 import BeautifulSoup
from progressbar import ProgressBar


book_list = ['16406','1342','2515','2489','9404']
api_address = 'http://www.gutenberg.org/cache/epub/{}/pg{}.html'
api_address2 = 'http://www.gutenberg.org/files/{}/{}-h/{}-h.htm'
i = 0
file_list = []
title = 'book_{}.txt'
pbar = ProgressBar()

for books in pbar(book_list):
    page = requests.get(api_address.format(books,books))
    if(page.status_code != 200):
        page = requests.get(api_address2.format(books,books,books))
        soup = BeautifulSoup(page.content,'html.parser')
        text = soup.find_all('p')
    else:
        soup = BeautifulSoup(page.content,'html.parser')
        text = soup.find_all('p')
        if(len(text)>54):
            text = text[54:len(text)-1]
    file = open(title.format(str(i)),'w')
    for te in text:
        file.write(str(te.string))  
    file.close()
    file_list.append(title.format(str(i)))
    i = i + 1
