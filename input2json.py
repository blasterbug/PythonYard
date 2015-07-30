#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Put into a json collection the input, the first argument is the collection
# name. The resultat is send to the default ouput.

import sys
import json
import argparse

# parser for CLI
parser = argparse.ArgumentParser( description='Process some data to JSON file' )
# adding some arguments
output_objt = parser.add_argument( '-o', '--ouput',
    help="Give a file name to store JSON ouputs",
    type=argparse.FileType('w'),
    default='tempory.json' )

parser.add_argument( '-i', '--input',
    help="The input file to process",
    type=argparse.FileType('r'),
    required=True )

# main i.e. do some processes
def main( filename, inputfile ) :
    # put the argv list in a json list
    jsdata = json.dumps( open( inputfile ), indent=True )
    # create a tempory file
    tmpfile = open( filename + ".json", "w")
    # store json data in file
    tmpfile.write( jsdata )
    # last char
    tmpfile.write( "\n" )
    # close file
    tmpfile.close()

# function called by default
if __name__ == "__main__" :
    args = parser.parse_args()
    print( output_objt )
    try :
        filename = sys.argv.pop( 0 )

        #main( filename, sys.argv )
    except IndexError :
        print( "Give a filename", file=sys.stderr )
