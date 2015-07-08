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
    dct = json.load( open( "words.json" ) )
    res = random.choice( dct['descriptive'] ) + " " + random.choice( dct['noums'] )
    print res
    print plain2leet( res )

if __name__ == "__main__" :
    main( sys.argv )
