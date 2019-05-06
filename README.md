This is a data aquisition frame work. It acquires and processes .txt files, parses them and produces two Pandas DataFrames. 

The first is an absolute table, telling you the proportion of total words each word is resposible (the idea being to acquire a probability 
distribution for the english language.

The second DataFrame is a conditional probability table, it takes the words that comprise a given percent (90% is default) of the total and
computes the word distribution based on the occurence of each word (ie the probability of a word following another).

The intention is to use this information to create a maximum-likelihood decoder based on the Viterbi algorithm for text.
