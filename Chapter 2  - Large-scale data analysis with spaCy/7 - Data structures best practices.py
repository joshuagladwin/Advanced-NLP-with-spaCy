# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:56:43 2019

@author: Josh
"""

'''
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

#Get all tokens and part-of-speech tags
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    #Check if the current token is a proper noun
    if pos == "PROPN"
    #Check if the next token is a verb
    if pos_tags[index + 1] == "VERB":
        result = token_texts[index]
        print("Found proper noun before a verb:", result)
'''
        
#Q: Why is the code bad?
        
#A: line 14, 15 use lists of strings; should use token attribute
        
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

for token in doc:
    #Check if the current token is a proper noun
    if token.pos_ == "PROPN":
    #Check if the next token is a verb
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)