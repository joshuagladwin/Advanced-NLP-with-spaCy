# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:17:41 2019

@author: Josh
"""

#Step 1

from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

##Register the Token extension attribute 'is_country' with the default value False
#Token.set_extension('is_country', default=False)
#
##Process the text and set the is_country attribute to True for the token "Spain"
#doc = nlp("I live in Spain")
#doc[3]._.is_country = True
#
##Print the token text and the is_country attribute for all tokens
#print([(token.text, token._.is_country) for token in doc])

#Step 2

def get_reversed(token):
    return token.text[::-1]

#Register the Token property extension 'reversed' with the getter get_reversed
Token.set_extension('reversed', getter=get_reversed)

#Process the text and print the reversed attribute for each token
doc = nlp("All generalizations are false, including this one.")
for token in doc:
    print("reversed:", token._.reversed)