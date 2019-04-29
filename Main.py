# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:32:17 2019

@author: Matthew Gill

The purpose of this script is to create a conditional probability database for the english language
At its core it is a text analyzer

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Functions
import constants

f = open('Declaration.txt','r')
content = f.read()

sentences = Functions.parse_Sentences(content)
absolute = {}
conditional = {}

for sent in sentences:
    [words,freq] = Functions.get_WordFrequency(Functions.parse_Words(sent))  
    for word in words:
        if(len(word)):        
            if word in list(absolute):
                absolute[word] = absolute[word] + freq[word]
            else:
                absolute[word] = freq[word]

df = pd.DataFrame(index = list(absolute),columns = ['Occurences'],data = list(absolute.values()))






"""
 Need to create a nxn matrix or pandas dataframe with words as column/row headers and the 
 cells as the following frequency
"""