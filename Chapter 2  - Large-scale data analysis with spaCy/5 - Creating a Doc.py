# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:47:45 2019

@author: Josh
"""

#Part 1

import spacy

nlp = spacy.load("en_core_web_sm")

#Import the Doc class
from spacy.tokens import Doc

#Desire text; "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

#Create a Doc from the words and space
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

#Part 2

#Desired text: "Go, get started!"
words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]

#Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

#Part 3

#Desired text: "Oh, really?!"
words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

#Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)