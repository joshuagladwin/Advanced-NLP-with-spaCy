# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:50:49 2019

@author: Josh
"""

#Example: a simple component (1)

import spacy

#Create the nlp object
nlp = spacy.load('en_core_web_sm')

#Define a custom component
def custom_component(doc):
    #Print the doc's length
    print('Doc length:', len(doc))
    #Return the doc object
    return doc

#Add the component first in the pipeline
nlp.add_pipe(custom_component, first=True)

#Print the pipeline component names
print('Pipeline:', nlp.pipe_names)

#Example a simple component (2)
doc = nlp("Hello World!")