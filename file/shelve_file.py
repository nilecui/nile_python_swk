#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-02-20 17:43
#       Filename: shelve.py
#    Description:
#****************************************************

import sys
import shelve

try:
    coutcredit=shelve.open("credit.dat")
except IOError:
    print >> sys.stderr,"File could not opened"
    sys.exit(1)
print "Enter acount number (1 to 100,0 to end input)"

while 1:
    accountNumber=int(raw_input("\nEnter account number\n?"))
    if 0 < accountNumber <= 100:
        print "Enter lastname, Firetname,balance"
        currentData=raw_input("?")
        coutcredit[str(accountNumber)]=currentData.split()
    elif accountNumber==0:
        break
coutcredit.close()
