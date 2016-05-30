#!/usr/bin/python3
# -*- coding: utf-8 -*-
# program I wrote to extract Umeå estate agencies data to JSON

import sys
import json
  
def read_file( file_name ) :
  """
  Read through a file and extract data
  
  :param file_name: name of the file containing the data set
  :return: dictionary with the data extracted
  """
  # open the file
  file_f = open( file_name, 'r' )
  # initiate a dictionary
  data = {}
  # for each line
  for line in file_f :
    i = 0
    # get the data on the line
    words = line.split()
    if len( words ) > 1 :
      company = words[i]
      i += 1
      # create an entry in the dictionary with the first data
      # and convert to integer the answer associated
      while not words[ i ].startswith( '0' ) : 
        company += " " + words[i]
        i += 1
      data[ company ] = {}
      # data[ company ]["company"] = company
      data[ company ]["phone"] = words[ i ]
      i += 1
      try:
          while words[ i ].isdigit() : 
            data[ company ]["phone"] += " " + words[i]
            i += 1
          data[ company ]["web"] = words[i]
      except :
        pass 
      print( company + " : " + data[ company ].__str__() )
  # return the dictionary
  return data

# function called by default
if __name__ == "__main__" :
  input_file = sys.argv[1]
  dic_data = read_file( input_file )
  # put the argv list in a json list
  jsdata = json.dumps( dic_data, indent=True, ensure_ascii=False, encoding="utf-8" )
  # create a tempory file
  tmpfile = open( input_file + ".json", 'w' )
  # store json data in file
  tmpfile.write( jsdata )
  # last char
  tmpfile.write( "\n" )
  # close file
  tmpfile.close()
