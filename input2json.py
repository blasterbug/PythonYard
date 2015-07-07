#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Put into a json collection the input, the first argument is the collection
# name. The resultat is send to the default ouput.

import os
import sys

def main( argv ):
    # delete program name
    argv.pop( 0 )
    # start fo the input, the collection name
    print( "{\n\t\"" + argv.pop( 0 ) + "\" : [")
    for value in argv:
        print( "\t\t\"" + value + "\"," )
    # close the collection
    print( "\t]\n}" )


if __name__ == "__main__":
    main( sys.argv )
#    print( "Finished shutdown." )
