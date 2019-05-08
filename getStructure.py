# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:29:25 2019
@author: Matthew
"""

import nltk as nl
import constants
import pandas as pd
import numpy as np

"""
print("Begin Aquisition")
import Aquisition
Files = Aquisition.file_list
print("Done Acqusition")

Tag	Meaning	English Examples
ADJ	adjective	new, good, high, special, big, local
ADP	adposition	on, of, at, with, by, into, under
ADV	adverb	really, already, still, early, now
CONJ	conjunction	and, or, but, if, while, although
DET	determiner, article	the, a, some, most, every, no, which
NOUN	noun	year, home, costs, time, Africa
NUM	numeral	twenty-four, fourth, 1991, 14:24
PRT	particle	at, on, out, over per, that, up, with
PRON	pronoun	he, their, her, its, my, I, us
VERB	verb	is, say, told, given, playing, would
.	punctuation marks	. , ; !
X	other	ersatz, esprit, dunno, gr8, univeristy
"""
parts = constants.parts
structure_absolute = pd.DataFrame(index = parts, columns = ['Prob','Occurences'], data = np.zeros([len(parts),2], dtype = int))


for file in Files:
    f = open(file,'r')
    content = f.read()
    f.close()
    sentences = Functions.parse_Sentences(content)
    pbar = ProgressBar()
    print("Begin File: " + file)
    for sent in pbar(sentences):
        text = nl.word_tokenize(sent)
        text = nl.pos_tag(text,tagset='universal')
        for te in text:
            if te[1] in parts:
                structure_absolute['Occurences'][te[1]] = structure_absolute['Occurences'][te[1]] + 1 

structure_absolute = structure_absolute.sort_values(['Occurences'],ascending=False)
structure_absolute['Prob'] = structure_absolute['Occurences']/structure_absolute['Occurences'].sum()
add = pd.DataFrame(index = list(structure_absolute.index), columns = ['Captured'])
add['Captured'][0] = structure_absolute['Prob'][0]
upper = structure_absolute.shape[0]-1

for i in range(1,upper):
    add['Captured'][i] = structure_absolute['Prob'][i] + add['Captured'][i-1]
add['Captured'][i] = 1
structure_absolute = pd.concat([structure_absolute,add],axis=1)
structure_absolute.to_excel("structure_absolute.xlsx")

structure_conditional = pd.DataFrame(index = parts, columns = parts, data = np.zeros([len(parts),len(parts)]),dtype = float)

for file in Files:
    f = open(file,'r')
    content = f.read()
    f.close()
    sentences = Functions.parse_Sentences(content)
    pbar = ProgressBar()
    print("Begin File: " + file)
    for sent in pbar(sentences):
        text = nl.word_tokenize(sent)
        text = nl.pos_tag(text,tagset='universal')
        for i in range(0,len(text)-2):
            word = text[i][1] 
            next_word = text[i+1][1]
            if word in parts and next_word in parts:
                    structure_conditional[word][next_word]= structure_conditional[word][next_word] + 1

for ind in list(structure_conditional.index):
    structure_conditional[ind] = structure_conditional[ind]/structure_conditional[ind].sum() 

structure_conditional.to_excel("structure_conditional.xlsx")







    