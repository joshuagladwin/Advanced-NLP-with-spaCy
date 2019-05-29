# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:59:36 2019

@author: Josh
"""

#Part 1

import spacy

nlp = spacy.load('en_core_web_sm')
text = (
        "Chick-fil-A is an American fast food restaurant headquartered in "
        "the city of College Park, Georgia, specializing in chicken sandwiches."
        )

#Only tokenise the text
doc = nlp.make_doc(text)
print([token.text for token in doc])

#Part 2

#Disable the tagger and parser
with nlp.disable_pipes('tagger', 'parser'):
    #Process the text
    doc = nlp(text)
    print(doc.ents)