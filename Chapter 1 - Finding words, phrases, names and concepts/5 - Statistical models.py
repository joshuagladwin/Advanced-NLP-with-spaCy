# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:21:37 2019

@author: Josh
"""

#Predicting Part-of-speech Tags

import spacy

#Load the small English model
nlp = spacy.load('en_core_web_sm')

#Process a text
doc = nlp("She ate the pizza")

#Iterate over the tokens
for token in doc:
    #Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)
    
#Predicting Syntactic Dependencies
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
    
#Predicting Named Entities

#Process a text
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

#Iterate over the predicted entities
for ent in doc.ents:
    print(ent.text, ent.label_)
    
#Tip: the explain method (Try these in the console)
spacy.explain('GPE')
spacy.explain('NNP')
spacy.explain('dobj')