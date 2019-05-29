# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:16:42 2019

@author: Josh
"""

import spacy
from spacy.tokens import Span

nlp = spacy.load('en_core_web_sm')

def get_wikipedia_url(span):
    #Get a Wikipedia URL if the span has one of the labels
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text

#Set the Span extention wikipedia_url using getter get_wikipedia url
Span.set_extension('wikipedia_url', getter=get_wikipedia_url)

doc = nlp(
        "In over fifty years from his very first recordings right through to his"
        "last album, David Bowie was at the vanguard of contemporary culture."
        )

for ent in doc.ents:
    #Print the text and Wikipedia URL of the entity
    print(ent.text, ent._.wikipedia_url)