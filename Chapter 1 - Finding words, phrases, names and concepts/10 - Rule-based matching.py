# -*- coding: utf-8 -*-
"""
Created on Sun May 19 10:47:59 2019

@author: Josh
"""

#Using the Matcher (1)

import spacy

#Import the Matcher
from spacy.matcher import Matcher

#Load a model and create the nlp object
nlp = spacy.load('en_core_web_sm')

#Initialise the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

#Add the pattern to the matcher
pattern = [{"ORTH": "iPhone"}, {"ORTH": "X"}]
matcher.add('IPHONE_PATTERN', None, pattern)

#Process some text
doc = nlp("New iPhone X release date leaked")

#Call the matcher on the doc
matches = matcher(doc)

#Using the Matcher (2)

#Iterate over the matches
for match_id, start, end in matches:
    #Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)