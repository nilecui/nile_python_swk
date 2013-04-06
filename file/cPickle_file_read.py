#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-02-20 18:00
#       Filename: cPickle_file_read.py
#    Description:
#****************************************************

import sys
import cPickle

try:
    outcredit=open("credit.dat","r")
except IOError:
    print >> sys.stderr,"File could not be opened"
    sys.exit(1)

records=cPickle.load(outcredit)
outcredit.close()
for record in records:
    print record[0].ljust(15),
    print record[1].ljust(10),
    print record[2].ljust(20)
