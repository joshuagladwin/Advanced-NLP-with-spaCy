# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:14:46 2019

@author: Josh
"""

#Similarity examples (1)

import spacy

nlp = spacy.load('en_core_web_md')

#Compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))

#Compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))

#Similarity examples (2)

#Compare a document with a token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))

#Compare a span with a document
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))

#Word vectors in spaCy

doc = nlp("I have a banana")
#Access the vector via the token.vector attribute
print(doc[3].vector)

#Similarity depends on the application context

doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))