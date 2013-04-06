#!/usr/bin/python
#-*- coding:utf-8 -*-

d={"book":"library",
        "page":250,
        "scripts":350}
print d

book="lb2"
pages=250
scripts=100

print "the %(book)s book contains more than %(scripts)s scripts"%vars()
