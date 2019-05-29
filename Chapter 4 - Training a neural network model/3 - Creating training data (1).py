# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:59:13 2019

@author: Josh
"""

import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open('iphone.json') as f:
    TEXTS = json.loads(f.read())
    
nlp = English()
matcher = Matcher(nlp.vocab)

#Two tokens whose lowercase forms match 'iPhone' and 'x'
pattern1 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

#Token whose lowercase form matches 'iphone' and an optional digit
pattern2 = [{'LOWER': 'iphone'}, {'IS_DIGIT': True, 'OP':'?'}]

#Add patterns to the matcher
matcher.add('GADGET', None, pattern1, pattern2)