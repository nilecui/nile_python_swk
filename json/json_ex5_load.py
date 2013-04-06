#!/usr/bin/python
#-*- coding:utf-8 -*-

import simplejson as json


f=open("test.json","r")
ls=f.read()
str=json.loads(ls)
print str
print str[0]
print str[1]
f.close
