#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-02-20 17:54
#       Filename: cPickle_file.py
#    Description:
#****************************************************

import sys
import cPickle

try:
    coutcredit=open("credit.dat","w")
except IOError:
    print >> sys.stderr,"File could not be opened"
    sys.exit(1)
print "Enter account number (1 to 100,0 to end input)"
inputlist=[]
while 1:
    try:
        accountline=raw_input("?")
    except EOFError:
        break
    else:
        inputlist.append(accountline.split())
        print inputlist
cPickle.dump(inputlist,coutcredit)
coutcredit.close()
