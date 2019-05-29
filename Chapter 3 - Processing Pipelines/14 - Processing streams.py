# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:34:28 2019

@author: Josh
"""

#Part 1

import json
import spacy

nlp = spacy.load('en_core_web_sm')

with open('tweets.json') as f:
    TEXTS = json.loads(f.read())
    
#Process the texts and print the adjectives
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])
    
#Part 2
    
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)

#Part 3

from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

#Create a list of patterns for the PhraseMatcher
patterns = list(nlp.pipe(people))