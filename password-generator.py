#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pick up two words and a json file and print them

import sys
import json
import random

def main( argv ) :
    dct = json.load( open( "words.json" ) )
    print( random.choice( dct['descriptive'] ) + " " + random.choice( dct['noums'] ) )

if __name__ == "__main__" :
    main( sys.argv )
