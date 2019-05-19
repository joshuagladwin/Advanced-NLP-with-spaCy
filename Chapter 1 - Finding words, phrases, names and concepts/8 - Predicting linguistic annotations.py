# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:00:57 2019

@author: Josh
"""

#Part 1

import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

#Process the text
doc = nlp(text)

#Print the document text
print(doc.text)

for token in doc:
    #Get the token text, part-of-speech tage, and the dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    
    print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))
    
#Part 2
for ent in doc.ents:
    #Print the entity text and its label
    print(ent.text, ent.label_)