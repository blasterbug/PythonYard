#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Read `words.json` and choose randomly a descriptive and a noun.
Then leetify it to create a password.
"""

__author__ = "Benjamin Sientzoff"
__version__ = "1.0"
__maintainer__ = "Benjamin Sientzoff (blasterbug)"
__license__ = "GNU GPL V2"

import sys
import json
import random
from leet import plain2leet


if __name__ == "__main__" :
    # read words from JSON file
    dct = json.load( open( "words.json" ) )
    # `dict` is a dictionnary where `descriptive` and `noums` lists are stored
    res = random.choice( dct['descriptive'] ) + " " + random.choice( dct['noums'] )
    print( "Original string :\t" + res )
    print( "Password :\t\t" + plain2leet( res ) )
    print( "Consider uppercase letters to increase strenght and a 8 digits long password" )
    
