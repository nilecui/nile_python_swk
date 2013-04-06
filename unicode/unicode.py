#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2012-12-18 16:23
#       Filename: unicode.py
#    Description:
#****************************************************

s1=u'哈'
print s1

s2=unicode('蛤','utf-8')
print s2

s3=u'test汉'
print repr(s3)

s4=s3.encode('utf-8')
print s4
