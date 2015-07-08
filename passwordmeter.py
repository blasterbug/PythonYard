#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Benjamin Sientzoff
# 2015/7/08
# Test and compute a password strenght

import sys
import string


def compute_strenght( password ) :
    alphaUP = 0
    alphaLO = 0
    number = 0
    repInc = 0
    repChar = 0
    lenghtP = len( password )
    strenght = lenghtP * 4
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
        divider = string.index( password, char ) - string.rindex( password, char )
        charCount = string.count( password, char, deb )
        if divider > 0 :
            repInc += abs( charcount / divider )
        if charCount > 0 :
            repChar += 1
    # compute general point
    if ( alphaUP > 0 ) and ( alphaUP < lenghtP ) :
        strenght += alphaUP + ( 2 * ( lenghtP - alphaUP ) )
    if ( alphaLO > 0 ) and ( alphaLO < lenghtP ) :
        strenght += alphaLO + ( 2  * ( lenghtP - alphaLO ) )
    if ( number> 0 ) and ( number < lenghtP ) :
        strenght += number + ( lenghtP - number )
    if repChar > 0 :
        strenght -= repChar
    if strenght > 100 :
        return "100% - Good password"
    elif strenght < 0 :
        return "0% - Weak password!"
    return strenght.__str__()  + "%"


if __name__ == "__main__" :
    print compute_strenght( sys.argv[1] )
