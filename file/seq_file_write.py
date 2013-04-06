#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-02-20 17:16
#       Filename: seq_file.py
#    Description:
#****************************************************

import sys

try:
    file=open('client.dat','aw')
except IOError,message:
    print >> sys.stderr,"File could not be opened!",message
    sys.exit(1)

print "Enter the account,name,and age."

while 1:
    try:
        accountline=raw_input("?")
    except EOFError:#ctrl+D
        break
    else:
        print >> file,accountline

file.close()
