#!/usr/bin/python
#-*- coding:utf-8 -*-

def load(f):
    if isinstance(f,type("")):
        file=open(f,"rb")
    else:
        print "file is empty"
    return file.read()

print load("hello.py")
print len(load("hello.py")),"bytes"
print len(load("hello.txt")),"bytes"
