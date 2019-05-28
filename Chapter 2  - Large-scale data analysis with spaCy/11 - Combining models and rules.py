# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:48:12 2019

@author: Josh
"""

#Adding statistical predictions

import spacy

from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)
matcher.add('DOG', None, [{'LOWER': 'golden'}, {'LOWER': 'retriever'}])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print('Matched span:', span.text)
    #Get the spans's root token and root head token
    print('Root token:', span.root.text)
    print('Root head token:', span.root.head.text)
    #Get the previous token and its POS tag
    print('Previous token:', doc[start - 1].text, doc[start - 1].pos_)
    
#Efficient phrase matching (2)

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add('DOG', None, pattern)
doc = nlp("I have a Golden Retriever")

#Iterate over the matches
for match_id, start, end in matcher(doc):
    #Get the matched span
    span = doc[start:end]
    print("Matched span:", span.text)