# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:16:52 2019

@author: Matthew
"""
import pandas as pd
import numpy as np
import nltk as nl
import Functions
import matplotlib.pyplot as plt
from progressbar import ProgressBar

removal = ['.',
  ' ',
',',
 '"',
';',
 ':',
'-',
' ',
'\n',
 '\r',
'&',
 '?',
"'",
'!',
']',
 '[',
'(',
')']

parts=['ADJ',
'ADP',	
'ADV',	
'CONJ',
'DET',
'NOUN',
'NUM',	
'PRT',	
'PRON',
'VERB',	
]



PERIOD = '.'
SPACE = ' '
COMMA  = ','
QUOTE = '"'
SEMI = ';'
COLON = ':'
DASH = '-'
SPACE = ' '
NEWLINE = '\n'
RESET = '\r'
AND = '&'
QUESTION = '?'
QUOTE1 = "'"
EXCLAIM = '!'
SQUAREO = ']'
SQUAREC = '['
CIRCO = '('
CIRCC = ')'

