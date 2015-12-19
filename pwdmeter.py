#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test and compute passwords strength
TODO: detect redundant pattern
"""
__author__ = "Benjamin Sientzoff"
__version__ = "0.2b"
__maintainer__ = "Benjamin Sientzoff (blasterbug)"
__license__ = "GNU GPL V2"

import sys
import string


def compute_strength( password ) :
    """
    Compute the strength of a password
    :param password: password to being tested
    :return: strengh of the password
    """
    alphaUP = 0
    alphaLO = 0
    number = 0
    repInc = 0
    repChar = 0
    lenghtP = len( password )
    strength = lenghtP * 4
    deb = 0
    comm = ''
    # check each char in password
    for char in password :
        deb += 1
        if char in string.ascii_uppercase :
            alphaUP += 1
        if char in string.ascii_lowercase :
            alphaLO += 1
        if char in string.digits :
            number += 1
        # compute icrement deduction base on prximity of repeated terms
        divider = password.find( char ) - password.rfind( char )
        charCount = password.count( char, deb )
        if divider > 0 :
            repInc += abs( charcount / divider )
        if charCount > 0 :
            repChar += 1
    # compute general point
    if ( alphaUP > 0 ) and ( alphaUP < lenghtP ) :
        strength += alphaUP + ( 2 * ( lenghtP - alphaUP ) )
    if ( alphaLO > 0 ) and ( alphaLO < lenghtP ) :
        strength += alphaLO + ( 2  * ( lenghtP - alphaLO ) )
    if ( number> 0 ) and ( number < lenghtP ) :
        strength += number + ( lenghtP - number )
    if repChar > 0 :
        strength -= repChar
    # display details
    # print( "Uppercase score :\t" + str( alphaUP + ( 2 * ( lenghtP - alphaUP ) ) ) )
    # print( "Lowercase score :\t" + str( alphaLO + ( 2  * ( lenghtP - alphaLO ) ) ) )
    # print( "Number score :\t" +  str( number + ( lenghtP - number ) ) )
    # display total score
    return strength


if __name__ == "__main__" :
    strength = compute_strength( sys.argv[1] )
    st = "Password strength : "
    if strength > 100 :
        print( st + "100% - Good password" )
    elif strength < 0 :
        print( st + "0% - Weak password!" )
    else :
        print( st + strength.__str__()  + "%" )
