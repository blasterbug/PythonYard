#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Benjamin Sientzoff
# 2015/7/08
# Pick up two words and a json file, print them and turn into a password

import sys
import json
import random
from leet import plain2leet

def main( argv ) :
    # read woreds from JSON file
    dct = json.load( open( "words.json" ) )
    # `dict` is a dictionnary where `descriptive` and `noums` lists are stored
    res = random.choice( dct['descriptive'] ) + " " + random.choice( dct['noums'] )
    print "Original string :\t" + res
    print "Password :\t\t" + plain2leet( res )

if __name__ == "__main__" :
    main( sys.argv )
    print "Consider uppercase letters to increase strenght and a 8 digits long password"
