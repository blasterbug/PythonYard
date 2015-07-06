#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main( argv ):
    for value in argv:
        print( value )
    print( "Finished shutdown." )


if __name__ == "__main__":
    main( sys.argv )
