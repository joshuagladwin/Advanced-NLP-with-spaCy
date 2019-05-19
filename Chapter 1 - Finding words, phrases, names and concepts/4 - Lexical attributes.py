# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:58:50 2019

@author: Josh
"""

from spacy.lang.en import English

nlp = English()

#Process the text
doc = nlp(
        "In 1990, more than 60% of people in East Asia were in extreme poverty. "
        "Now less than 4% are."    
        )

#Iterate over the tokens in the doc
for token in doc:
    #Check if the token resembles a number
    if token.like_num:
        next_token = doc[token.i + 1]
        #Check if the next token's text equals '%'
        if next_token.text == "%":
            print("Percentage found:", token.text)