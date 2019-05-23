# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:16:33 2019

@author: Josh
"""

import spacy


#Load the en_core_web_md model

nlp = spacy.load('en_core_web_md')

#Prcoess a text

doc = nlp("Two bananas in pyjamas")

#Get the vector for the token "bananas"
banana_vector = doc[1].vector
print(banana_vector)