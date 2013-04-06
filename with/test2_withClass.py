#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2012-12-06 14:29
#       Filename: test2_withClass.py
#    Description:
#****************************************************
class A:
    def __enter__(self):
        print 'in enter'

    def __exit__(self,e_t,e_v,e_b):
        print 'in exit'

with A() as a:
    print 'in with'

