#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-19 09:32
#       Filename: json_dumps_encoding.py
#    Description:
#****************************************************

import json


#python -----------json
#dict              obj
#list,tuple        array
#str,unicode       string
#int,long,float    number
#True              true
#Flase             false
#None              Null

if __name__=="__main__":
    obj=[['a','b','c'],[1,2,3],123,4000.95,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
    #json.dumps()方法返回一个str对象
    encodedjson=json.dumps(obj)
    #repr是给编译器看的
    #str是给人看的

    print "repr(obj):",repr(obj)
    print "encodedjson:",encodedjson



