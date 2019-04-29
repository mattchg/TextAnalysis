# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:48:35 2019

@author: Matthew
"""
import constants
from collections import OrderedDict


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
    word = drop_nonalpha(word, constants.COLON)
    word = drop_nonalpha(word, constants.COMMA)  
    word = drop_nonalpha(word, constants.DASH)
    word = drop_nonalpha(word, constants.PERIOD)
    word = drop_nonalpha(word, constants.QUOTE)
    word = drop_nonalpha(word, constants.SEMI)
    word = drop_nonalpha(word, constants.SPACE)
    word = drop_nonalpha(word, constants.NEWLINE)
    word = drop_nonalpha(word, constants.RESET)
    return str(word.lower())    

def drop_nonalpha (word, part):
    while(word.partition(part)[1]):
        if(word.partition(part)[0] == ''):
            word = word.partition(part)[2]
        else:
            word = word.partition(part)[0]
    return word


def get_WordFrequency(words):
    #remove duplicates
    words_no_dupe = list(OrderedDict.fromkeys(words))
    freq  = {}    
    for word in words_no_dupe:
        freq[word] = words.count(word)
    return [words_no_dupe, freq]
    