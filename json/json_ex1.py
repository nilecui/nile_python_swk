#!/usr/bin/python
#-*- coding:utf-8 -*-

import simplejson as json


t=json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
print t

f=open("test.json","w")

f.write(t)
f.close()
