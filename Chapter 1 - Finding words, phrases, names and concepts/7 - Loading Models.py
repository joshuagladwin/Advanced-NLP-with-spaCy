# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:51:20 2019

@author: Josh
"""

import spacy

#Load the 'en_core_web_sm' model

nlp = spacy.load('en_core_web_sm')

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

#Process the text
doc = nlp(text)

#Print the document text
print(doc.text)