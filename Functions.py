# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:48:35 2019

@author: Matthew
"""
import constants

def parse_Sentences(text_Body):
  text = str(text_Body)
  sentences = []
  while text.partition(constants.PERIOD)[2]: #Check if it only one sentence
      sentences.append(text.partition(constants.PERIOD)[0])
      text = text.partition(constants.PERIOD)[2]
  sentences.append(text)
  return sentences

def parse_Words(sentence):
  words = []
  while sentence.partition(constants.SPACE)[2]: #Check if it only one word
      word = scrub_word(sentence.partition(constants.SPACE)[0])
      words.append(word)
      sentence = sentence.partition(constants.SPACE)[2]
  words.append(scrub_word(sentence))
  return words
  
def scrub_word(word):
    for element in constants.removal:
        word = drop_nonalpha(word,element)
    if(word.isalpha()):
        return str(word.lower())
    else:
        return ''
def drop_nonalpha (word, part):
    while(word.partition(part)[1]):
        if(word.partition(part)[0] == ''):
            word = word.partition(part)[2]
        else:
            word = word.partition(part)[0]
    return word


def get_WordFrequency(words):
    from collections import OrderedDict
    words_no_dupe = list(OrderedDict.fromkeys(words))
    freq  = {}    
    for word in words_no_dupe:
        freq[word] = words.count(word)
    return [words_no_dupe, freq]

def create_conditional_dictionary(conditional,words):
    pbar = ProgressBar()
    if(len(conditional)):
        for word in pbar(words):
            if not(word in list(conditional)):
                conditional[word] = dict(zip(words, [0]*len(words)))
                for element in list(conditional):
                    conditional[element][word] = 0
        return conditional
    else:
        dictionary = dict(zip(words, [0]*len(words)))
        for word in words:
                dictionary[word] = dict(zip(words, [0]*len(words)))    
        return dictionary
    
def create_conditional_dataframe(conditional, word_list):
    import pandas as pd
    pbar = ProgressBar()
    print("Creating Conditional Dataframe")
    df = pd.DataFrame(index = word_list, columns = word_list)
    print("Created empty Dataframe")
    
    for word in pbar(word_list):
        df[word] = list(conditional[word].values())
    return df

def create_absolute_dataframe(absolute):
    import pandas as pd
    return pd.DataFrame(index = list(absolute),columns = ['Occurences'],data = list(absolute.values()))


def create_absolute_dictionary(df):
    return dict(zip(df.index.map(str), list(df['Occurences'])))

def analyze_sentence(sentence):
    return nl.pos_tag(nl.word_tokenize(sentence),tagset='universal')