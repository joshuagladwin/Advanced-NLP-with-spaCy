# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:54:51 2019

@author: Josh
"""

import json
from spacy.lang.en import English
from spacy.tokens import Doc

with open('bookquotes.json') as f:
    DATA = json.loads(f.read())

nlp = English()

#Register the Doc extension 'author' (default None)
Doc.set_extension('author', default=None)

#Register the Doc extension 'book' (default None)
Doc.set_extension('book', default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    #Set the doc._.book and doc._.author attributes from the context
    doc._.book = context['book']
    doc._.author = context['author']
    
    print(doc.text, '\n', '- "{}" by {}'.format(doc._.book, doc._.author), '\n')