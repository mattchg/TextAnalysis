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
      words.append(sentence.partition(constants.SPACE)[0].lower())
      sentence = sentence.partition(constants.SPACE)[2]
  words.append(sentence.lower())
  return words

  