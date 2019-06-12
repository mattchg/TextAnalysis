▪	A Python tool that processes English language text from the Project Guttenberg website to create a probability distribution for written English text
  o	  For applications to text-prediction tools
▪	Utilizes web scraping tools in Python (BeautifulSoup) to automate the capture of the text from the Raw HTML
▪	Creates custom text processing tools to parse text into sentences and words 
▪	Efficiently processed the data to create both absolute and conditional probability tables
    o	 Processed ten books to obtain ~50,000 unique words
▪	Created a basic text prediction tool based on the acquired data

This is a data aquisition frame work. It acquires and processes .txt files, parses them and produces two Pandas DataFrames. 

absolute table: The proportion of total words each word is resposible (the idea being to acquire a probability 
distribution for the english language.

conditional probability table: it takes the words that comprise a given percent (90% is default) of the total and
computes the word distribution based on the occurence of each word (ie the probability of a word following another).

The intention is to use this information to create a maximum-likelihood decoder based on the Viterbi algorithm for text.

To use it, clone the repo, and run the get_absolute() script, it calls the rest, the tables will be saved in the directory.
