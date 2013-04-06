#!/usr/bin/python
#-*- coding:utf-8 -*-

def addlist(alist):
    print "addlist-->"
    for i in alist:
        print "-------------\n"
        print i
        yield i+1

a=[1,2,3,4]
print addlist(a)

print "=="*30
a1=[1,2,3,4]
for x in addlist(a1):
    print "x=",x
