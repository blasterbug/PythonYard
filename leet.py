#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Transform plain text to a sort of leet
Th table below is used to perform the translation
plain text | l33t
-----------|------
    ' '    |  ''
    'a'    |  '4'
    'b'    |  '6'
    'c'    | '('
    'e'    | '3'
    'i'    | '!'
    'l'    | '1'
    'o'    | '0' 
    's'    | '5'
    't'    | '7'
    'z'    | '2'
"""
__author__ = "Benjamin Sientzoff"
__version__ = "0.1b"
__maintainer__ = "Benjamin Sientzoff (blasterbug)"
__license__ = "GNU GPL V2"

def char2leet( char ) :
    """
    Macth a regular char to a 133t one according to the matching array
    :param char: plain character to convert
    :return: matching leet character
    """
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


def leet2char( char ) :
    """
    Macth a leet char to a plain one according to the matching array
    :param char: leet character to convert
    :return: matching plain character
    """
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

def plain2leet( string ) :
    """
    Transform a string to sort of 133t (leet)
    :param string: plain string to convert
    :return: matching leet string
    """
    if len(string) == 1 :
        return char2leet( string )
    else :
        return char2leet( string[0] ) +  plain2leet( string[1:] )

def leet2plain( string ) :
    """
    Transform a leet string to plein text
    :param string: leet string to convert
    :return: matching plain string
    """
    if len(string) == 1 :
        return leet2char( string )
    else :
        return leet2char( string[0] ) +  leet2plain( string[1:] )
