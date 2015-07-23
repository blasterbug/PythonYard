#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Put into a json collection the input, the first argument is the collection
# name. The resultat is send to the default ouput.

import sys
import json


def main( argv ) :
    # delete program name
    argv.pop( 0 )
    # put the argv list in a json list
    jsdata = json.dumps( argv, indent=True )
    # create a tempory file
    tmpfile = open( "tempory.json", "w")
    # store json data in file
    tmpfile.write( jsdata )
    # last char
    tmpfile.write( "\n" )
    # close file
    tmpfile.close()

if __name__ == "__main__" :
    main( sys.argv )
#    print( "Finished shutdown." )
