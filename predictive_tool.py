# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:03:18 2019

@author: Matthew
"""

import pandas as pd
import numpy as np
import nltk as nl
import Functions
import matplotlib.pyplot as plt
from progressbar import ProgressBar

"""
word_absolute = pd.read_excel('absolute.xlsx', index_col = 0)
print("Done: word_absolute")
word_conditional = pd.read_excel('conditional.xlsx',index_col = 0)
print("Done: word_conditional")
structure_absolute = pd.read_excel('structure_absolute.xlsx',index_col = 0)
print("Done: structure_absolute")
structure_conditional = pd.read_excel('structure_conditional.xlsx',index_col = 0)
"""


sent = 'yes I below'
text = nl.word_tokenize(sent)
text = nl.pos_tag(text,tagset='universal')
last_word = text[len(text)-1][0]
last_pos = text[len(text)-1][1]

ml_words = word_conditional[last_word].sort_values(ascending = False)
ml_words = ml_words[0:25]

ml_pos = structure_conditional[last_pos].sort_values(ascending = False)
ml_pos = ml_pos[ml_pos >= 0.05]
df = pd.DataFrame(index = list(ml_words.index), columns = ['P(word)','POS','P(POS)','P(TOT)'])
df['P(word)']= ml_words

for word in list(df.index):
    sentence = sent + ' ' + word
    text = nl.word_tokenize(sentence)
    text = nl.pos_tag(text,tagset='universal')
    last_pos = text[len(text)-1][1]
    if last_pos in ml_pos:    
        df['POS'][word] = last_pos
        df['P(POS)'][word] = ml_pos[last_pos]

df['P(TOT)'] =df['P(word)']*df['P(POS)'] 
df = df.sort_values(['P(TOT)'], ascending = False)
