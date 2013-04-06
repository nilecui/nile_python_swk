#!/usr/bin/python
#-*- coding:utf-8 -*-

import gdbm

db=gdbm.open("gdbm","c")

db["1"]="call"
db["2"]="thre"
db["3"]="next"
db["4"]="defendant"
db.close()

db=gdbm.open("gdbm","r")

keys=db.keys()
print "keys=",keys
print "排序中..."
keys.sort()

for key in keys:
    print db[key]
