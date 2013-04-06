#!/usr/bin/python
#-*- coding:utf-8-*-

class A:
    pass

class B:
    pass

class C(A):
    pass

class D(A,B):
    pass

def dump(oj):
    print oj,"=>",
    if issubclass(oj,A):
        print "A",
    if issubclass(oj,B):
        print "B",
    if issubclass(oj,C):
        print "C",
    if issubclass(oj,D):
        print "D",
    print

dump(A)
dump(B)
dump(C)
dump(D)
dump(0)
dump("string")
