#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2012-12-06 14:35
#       Filename: test3_contextmanager.py
#    Description:
#****************************************************
from contextlib import contextmanager
#from __future__ import with_statement

@contextmanager
def context():
    print 'enter the zone'
    try:
        yield
    except Exception,e:
        print 'with an error %s'%d
        raise e
    else:
        print 'with no error'

with context():
    print '----in context call ----'
