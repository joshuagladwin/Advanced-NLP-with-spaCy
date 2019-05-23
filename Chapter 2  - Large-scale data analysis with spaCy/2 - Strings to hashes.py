# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:34:09 2019

@author: Josh
"""

#Part 1

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I have a cat")

#Look up the hash for the word "cat"
cat_hash = nlp.vocab.strings['cat']
print(cat_hash)

#Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)

#Part 2

doc = nlp("David Bowie is a PERSON")

#Look up the hash for the string label "PERSON"
person_hash = nlp.vocab.strings['PERSON']
print(person_hash)

#Look up the person_hash to get the string
person_string = nlp.vocab.strings[person_hash]
print(person_string)