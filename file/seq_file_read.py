#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-02-20 17:20
#       Filename: seq_file_read.py
#    Description:
#****************************************************

import sys

try:
    file=open('./client.dat','r')
except IOError:
    print >>sys.stderr,"File could not be opened!"
    sys.exit(1)

records=file.readlines()

str1="Account".ljust(10)
str2="Name".ljust(10)
str3="age".ljust(10)

print str1+str2+str3

for record in records:
    fields=record.split()
    print fields[0].ljust(10),
    print fields[1].ljust(10),
    print fields[2].ljust(10)
file.close()
