# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:06:25 2019

@author: Josh
"""

#Step 1

#Import the English language class and create the nlp object
from spacy.lang.en import English

nlp = English()

#Process the text
doc = nlp("I like tree kangaroos and narwhals.")

#Select the first token
first_token = doc[0]

#Print the first token's text
print(first_token.text)

#Step 2

#Import the English language class and create the nlp object
from spacy.lang.en import English

nlp = English()

#Process the text
doc = nlp("I like tree kangaroos and narwhals.")

#A slice of the Doc for "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

#A slice of the doc for "tree kangaroos and narwhals" (without the ".")
tree_kangaroos_and_narwhals = doc[2:-1]
print(tree_kangaroos_and_narwhals.text)