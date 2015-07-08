#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pick up two words and a json file and print them

import sys
import json
import random

# macth a regular char to a 133t one
def leetmatchor( char ) :
    return {
        ' ' : '',
        'a' : '4',
        'b' : '6',
        'c' : '(',
        'e' : '3',
        'h' : 'h',
        'i' : '!',
        'l' : '1',
        'o' : '0',
        'p' : 'p',
        'q' : 'q',
        'r' : 'r',
        's' : '5',
        't' : '7',
        'z' : '2',
    }.get( char , char ) # default case

# transforme a string to sort of 133t (leet)
def plain2leet( string ) :
    leetified = list( '' )
    for char in string:
        leetified.append( leetmatchor( char ) )
    return ''.join( leetified )

def main( argv ) :
    dct = json.load( open( "words.json" ) )
    res = random.choice( dct['descriptive'] ) + " " + random.choice( dct['noums'] )
    print res
    print plain2leet( res )

if __name__ == "__main__" :
    main( sys.argv )
