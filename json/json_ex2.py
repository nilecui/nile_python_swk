#!/usr/bin/python
#-*- coding:utf-8 -*-

import simplejson as json


t=json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
print t

print json.dumps("\"foo\bar")
#设置排序字典
print json.dumps({"c":0,"b":1,"a":3},sort_keys=True)

#创建文件流对象
#from StringIO import StringIO
#io=StringIO()
#把json编码数据导向到此文件中
#json.dump(["streaming API",io]

#取得文件流对象的内容

f=open("test.json","w")

f.write(t)
f.close()
