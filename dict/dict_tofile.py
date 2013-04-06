#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-02-20 17:10
#       Filename: dict_tofile.py
#    Description:
#****************************************************

yourDict={'1000':{'1':['a','b','c','d'],'2':['e','b','c','a']},'2000':{'1':['c','d','c','d'],'2':['a','a','c','d']}}
out=open('out.xls','w')
for key in yourDict:
    out.write(key)
    for key2 in yourDict[key]:
        out.write('\t')
        out.write(key2+'\t')
        out.write('\t'.join(yourDict[key][key2] ))
        out.write('\n')
