# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:32:17 2019

@author: Matthew Gill

The purpose of this script is to create a conditional probability database for the english language

"""
import constants


print("Begin Aquisition")
import Aquisition


Files = Aquisition.file_list
absolute = {}
conditional = {}

print("Done Acqusition")

for file in Files:
    f = open(file,'r')
    content = f.read()
    f.close()
    pbar = ProgressBar()
    print("Begin File: " + file)
    sentences = Functions.parse_Sentences(content)
    for sent in pbar(sentences):
        [words,freq] = Functions.get_WordFrequency(Functions.parse_Words(sent))  
        for word in words:
            if(len(word)):        
                if word in list(absolute):
                    absolute[word] = absolute[word] + freq[word]
                else:
                    absolute[word] = freq[word]
    print("Done absolute: "+ file)


absolute_df = Functions.create_absolute_dataframe(absolute)
absolute_df = absolute_df.sort_values(['Occurences'], ascending = False)
word_list = list(absolute_df.index)
print("Created Absolute df ")

probability = pd.DataFrame(index = word_list, columns = ['Prob','Captured'], data = np.zeros([len(word_list),2], dtype = float))                   
for word in word_list:
    probability['Prob'][word] = absolute_df['Occurences'][word]/absolute_df['Occurences'].sum()
    probability['Captured'][word] = probability['Prob'].sum()


absolute_df = pd.concat([absolute_df,probability], axis = 1)
absolute_df.to_excel("absolute.xlsx")
print("Saved Absolute df ")             