# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:23:34 2019

@author: Josh
"""

#Part 1

import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

#Get the similarity of doc1 and doc2
similarity = doc1.similarity(doc2)
print(similarity)

#Part 2

doc = nlp("TV and books")
token1, token2 = doc[0], doc[1]

#Get similarity of the tokens "TV" and "books"
similarity = token1.similarity(token2)
print(similarity)

#Part 3

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

#Create spans for "great restaurant" and "really nice bar"
span1 = doc[3:5] 
span2 = doc[12:15]

#Get similarity of the spans
similarity = span1.similarity(span2)
print(similarity)