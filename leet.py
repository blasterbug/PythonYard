#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Benjamin Sientzoff
# 2015/7/08
# transform plin text to a sort of leet

# macth a regular char to a 133t one
def leetmatchor( char ) :
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

# transforme a string to sort of 133t (leet)
def plain2leet( string ) :
    leetified = list( '' )
    for char in string:
        leetified.append( leetmatchor( char ) )
    return ''.join( leetified )
