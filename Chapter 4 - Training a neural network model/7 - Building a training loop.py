# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:15:05 2019

@author: Josh
"""

import spacy
import random
import json

with open('gadgets.json') as f:
    TRAINING_DATA = json.loads(f.read())

#Create a blank 'en' model

nlp = spacy.blank('en')

#Create a new entity recogniser and add it to the pipeline
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

#Add the label 'GADGET' to the entity recogniser
ner.add_label('GADGET')

#Start the training
nlp.begin_training()

#Loop for 10 iterations
for itn in range(10):
    #Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}
    
    #Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]
        
        #Update the model
        nlp.update(texts, annotations, losses=losses)
        print(losses)