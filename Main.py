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

Files = ['Declaration.txt','HG.txt', 'Hawthorne.txt']
absolute = {}

for file in Files:
    f = open(file,'r')
    content = f.read()
    #absolute_df = pd.read_excel(open('absolute.xlsx', 'rb'), sheet_name = "Sheet1")
    sentences = Functions.parse_Sentences(content)
    #absolute = Functions.create_absolute_dictionary(absolute_df)
    
    for sent in sentences:
        [words,freq] = Functions.get_WordFrequency(Functions.parse_Words(sent))  
        for word in words:
            if(len(word)):        
                if word in list(absolute):
                    absolute[word] = absolute[word] + freq[word]
                else:
                    absolute[word] = freq[word]
    
    
    conditional = Functions.create_conditional_dictionary(list(absolute))
    
    for sent in sentences:
        words = Functions.parse_Words(sent)  
        for i in range(0,len(words)):
            word = words[i]
            if(len(word) and i != (len(words)-1)):        
                next_word = words[i+1]
                if (word in list(conditional) and next_word):
                    if(next_word in list(conditional[word])):
                        conditional[word][next_word] = conditional[word][next_word] + 1
                    else:
                        conditional[word][next_word] = 1     
    
    absolute_df = Functions.create_absolute_dataframe(absolute)                    
    conditional_df = Functions.create_conditional_dataframe(conditional,list(absolute))
    
    #absolute_df.to_excel("absolute.xlsx")
    #conditional_df.to_excel("conditional.xlsx")

