# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:16:46 2019

@author: Josh
"""

import spacy

#Import the Matcher
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
doc = nlp("New iPhone X release date leaked as Apple reveals pre-orders by mistake")

#Initialise the Matcher with the shared vocabulary
matcher  = Matcher(nlp.vocab)

#Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{"ORTH": "iPhone"}, {"ORTH": "X"}]

#Add the pattern to the matcher
matcher.add('IPHONE_PATTERN', None, pattern)

#Use the matcher on the doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])