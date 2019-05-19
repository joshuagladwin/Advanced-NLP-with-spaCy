# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:55:33 2019

@author: Josh
"""

#Part 1: English

#Import the English language class
from spacy.lang.en import English

#Create the nlp object
nlp = English()

#Process a text
doc= nlp("This is a sentence")

#Print the document text
print(doc.text)

#Part 2: German

#Import the German language class
from spacy.lang.de import German

#Create the nlp object
nlp = German()

#Process a text
doc = nlp("Liebe Grüße!")

#Print the document text
print(doc.text)

#Part 3: Spanish

#Import the Spanish language class
from spacy.lang.es import Spanish

#Create the nlp object
nlp = Spanish()

#Process a text
doc= nlp("¿Cómo estás?")

#Print the document text
print(doc.text)