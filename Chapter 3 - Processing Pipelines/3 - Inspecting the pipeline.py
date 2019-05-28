# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:23:00 2019

@author: Josh
"""

import spacy

#Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

#Print the names of the pipeline components
print(nlp.pipe_names)

#Print the full pipeline of (name, component) tuples
print(nlp.pipeline)