# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:47:57 2019

@author: Josh
"""

import spacy

nlp = spacy.load("en_core_web_sm")

#Shared vocab and string store (1)

doc = nlp("I love coffee")

coffee_hash = nlp.vocab.strings['coffee']
coffee_string = nlp.vocab.strings[coffee_hash]

#Raises an error if we haven't seen the string before
string = nlp.vocab.strings[3197928453018144401]

#Shared vocab and string store (2)

#Look up the string and hash in nlp.vocab.strings
print('hash value:', nlp.vocab.strings['coffee'])
print('string value:', nlp.vocab.strings[3197928453018144401])

#The doc also exposes the vocab and strings
print('hash value:', doc.vocab.strings['coffee'])

#Lexeme: entries in the vocabulary

lexeme = nlp.vocab['coffee']

#Print the lexical attributes
print(lexeme.text, lexeme.orth, lexeme.is_alpha)