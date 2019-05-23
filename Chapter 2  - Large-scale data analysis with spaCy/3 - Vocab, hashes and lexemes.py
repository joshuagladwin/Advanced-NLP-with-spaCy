# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:13:17 2019

@author: Josh
"""

#Q: Why does this code throw an error?

from spacy.lang.en import English
from spacy.lang.de import German

# Create an English and German nlp object
nlp = English()
nlp_de = German()

# Get the ID for the string 'Bowie'
bowie_id = nlp.vocab.strings['Bowie']
print(bowie_id)

# Look up the ID for 'Bowie' in the vocab
print(nlp_de.vocab.strings[bowie_id])

''' A: The string 'Bowie' is added to the English vocab (nlp)
    but the look-up uses the German vocab (nlp_de).
    As Bowie hasn't been added to the German vocab, it cannot
    look up 'Bowie' in the German vocab, so throws up the error.
'''    