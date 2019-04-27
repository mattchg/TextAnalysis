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

data = pd.read_csv('Test.txt', sep=".", header=None)

