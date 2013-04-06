#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2012-12-17 16:42
#       Filename: my_split.py
#    Description:
#****************************************************

s1='123,456,789,abc,cde'
s2=','
print s1.find(s2)

s1=s1[s1.find(s2)+1:]
print s1.find(s2)
print s1

s1=s1[s1.find(s2)+1:]
print s1.find(s2)
print s1

s1=s1[s1.find(s2)+1:]
print s1.find(s2)
print s1

s1=s1[s1.find(s2)+1:]
print s1.find(s2)
print s1

print s1
print "*"*30
s1='123,456,789,abc,cde'

for c in s1:
    if c in s2:
        nPos=s1.index(c)
        s1=s1[nPos+1:]
        print s1
        print nPos
