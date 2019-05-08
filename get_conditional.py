# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:54:21 2019

@author: Matthew
"""
import pandas as pd
import numpy as np
import nltk as nl
import Functions
import matplotlib.pyplot as plt
from progressbar import ProgressBar
import constants

print("Begin Aquisition")
import Aquisition
Files = Aquisition.file_list
print("Done Acqusition")

absolute = pd.read_excel("absolute.xlsx",index_col = 0)
conditional_list = absolute[absolute['Captured'] <= 0.90]
conditional_list = conditional_list['Occurences']
word_list = list(conditional_list.index)
conditional_df = pd.DataFrame(index = word_list, columns = word_list, data = np.zeros([len(word_list),len(word_list)]))

for file in Files:
    f = open(file,'r')
    content = f.read()
    f.close()
    pbar = ProgressBar()
    print("Begin File: " + file)
    sentences = Functions.parse_Sentences(content)
    for sent in pbar(sentences):
        words = Functions.parse_Words(sent)  
        for i in range(0,len(words)-2):
            word = words[i]
            next_word = words[i+1]
            if(word in word_list and next_word in word_list):        
                conditional_df[word][next_word] = conditional_df[word][next_word] + 1
    print("Updated Conditional: "+ file)

for word in word_list:
    conditional_df[word] = conditional_df[word]/conditional_df[word].sum()


conditional_df.to_excel('data.xls', sheet_name='Sheet1', index=False, engine='xlsxwriter')












