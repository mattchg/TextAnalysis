# -*- coding: utf-8 -*-
"""
This acquires the book texts from the project gutenburg website specified by the numbers in the list
book_list
It gathers the html, and parses it into text files for processing by the other scripts
"""
import requests
from bs4 import BeautifulSoup
from progressbar import ProgressBar


book_list = ['16406','59447','11','1661','74','174','1232','2515','36','996','20','521','2489']
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
        try: 
            file.write(str(te.string))
        except UnicodeEncodeError:
            x = 1
            #print("UnicodeError")
    file.close()
    file_list.append(title.format(str(i)))
    i = i + 1
