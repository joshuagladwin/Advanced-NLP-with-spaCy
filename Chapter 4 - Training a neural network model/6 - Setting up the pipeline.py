# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:15:05 2019

@author: Josh
"""

import spacy

#Create a blank 'en' model

nlp = spacy.blank('en')

#Create a new entity recogniser and add it to the pipeline
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

#Add the label 'GADGET' to the entity recogniser
ner.add_label('GADGET')