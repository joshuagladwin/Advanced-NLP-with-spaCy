# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:26:55 2019

@author: Josh
"""

#The Doc object

#Create an nlp object
from spacy.lang.en import English
nlp = English()

#Import the Doc class
from spacy.tokens import Doc

#The words and spaces to create the doc fro
words = ['Hello', 'world', '!']
spaces = [True, False, False]

#Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)

#The Span object

#Import the Span classes
from spacy.tokens import Span

#Create a span manually
span = Span(doc, 0, 2)

#Create a span with a label
span_with_label = Span(doc, 0, 2, label="GREETING")

#Add span to the doc.ents
doc.ents = [span_with_label]