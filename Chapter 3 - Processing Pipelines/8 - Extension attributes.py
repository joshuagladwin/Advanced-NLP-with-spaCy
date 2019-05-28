# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:44:21 2019

@author: Josh
"""
#Property extensions (1)

import spacy
from spacy.tokens import Token

nlp = spacy.load('en_core_web_sm')

#Defubte getter function
def get_is_color(token):
    colors = ['red', 'yellow', 'blue']
    return token.text in colors

#Set extension on the Token with getter
Token.set_extension('is_color', getter=get_is_color)

doc = nlp("The sky is blue")
print(doc[3]._.is_color, '-', doc[3].text)

#Property extensions (2)

from spacy.tokens import Span

#Define getter function
def get_has_color(span):
    colors = ['red', 'yellow', 'blue']
    return any(token.text in colors for token in span)

#Set extension on the Span with getter
Span.set_extension('has_color', getter=get_has_color)

print(doc[1:4]._.has_color, '-', doc[1:4].text)
print(doc[0:2]._.has_color, '-', doc[0:2].text)

#Method extensions

from spacy.tokens import Doc

#Define method with arguments
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

#Set extension on the Doc with method
Doc.set_extension('has_token', method=has_token)

print(doc._.has_token('blue'), ' - blue')
print(doc._.has_token('cloud'), ' - cloud')