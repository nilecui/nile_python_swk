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
#list              array
#unicode           string
#int,long          number(int)
#float             number(real)
#True              true
#Flase             false
#None              Null

if __name__=="__main__":
    print "---json.dumps---"*3
    obj=[['a','b','c'],[1,2,3],123,4000.95,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
    #json.dumps()方法返回一个str对象
    encodedjson=json.dumps(obj)
    #repr是给编译器看的
    #str是给人看的

    print "repr(obj):",repr(obj)
    print "encodedjson type:",type(encodedjson)
    print "encodedjson:",encodedjson

    print "---json.loads---"*3
    decodejson=json.loads(encodedjson)
    print "decodejson type:",type(decodejson)
    print "decodejson[4]['key1']:",decodejson[5]['key1']
    print "decodejson:",decodejson

