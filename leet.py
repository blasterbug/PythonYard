#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Benjamin Sientzoff
# 2015/7/08
# transform plin text to a sort of leet

# macth a regular char to a 133t one
def char2leet( char ) :
    return {
        ' ' : '',
        'a' : '4',
        'b' : '6',
        'c' : '(',
        'e' : '3',
        'i' : '!',
        'l' : '1',
        'o' : '0',
        's' : '5',
        't' : '7',
        'z' : '2',
    }.get( char , char ) # default case

# undo a leet conversion
def leet2char( char ) :
    return {
        '4' : 'a',
        '6' : 'b',
        '(' : 'c',
        '3' : 'e',
        '!' : 'i',
        '1' : 'l',
        '0' : 'o',
        '5' : 's',
        '7' : 't',
        '2' : 'z',
    }.get( char , char ) # default case

# transform a string to sort of 133t (leet)
def plain2leet( string ) :
    leetified = list( '' )
    for char in string :
        leetified.append( char2leet( char ) )
    return ''.join( leetified )

# get a string from a leet one
def leet2plain( string ) :
    unleet = list()
    for char in string :
        unleet.append( leet2char( char ) )
    return ''.join( unleet )
