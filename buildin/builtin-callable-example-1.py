#!/usr/bin/python
#-*- coding:utf-8 -*-

def dump(f):
    if callable(f):
        print f,"is callable"
        return 1
    else:
        print f,"is not* callable"
        return 0


class A:
    def method(self,v):
        return v

class B(A):
    def __call__(self,value):#可调用的
        print "*********call**********"
        return value
a=A()
b=B()

dump(0)
dump("string")

print "********************************"
dump(callable)
dump(dump)

print "********************************"
dump(A)
dump(B)
dump(B.method)
dump(A.method)
print "********************************"
dump(a)
dump(b)
print "********************************"

#直接调用call
if dump(b) :
    b(1)
else:
    print "b不是可调用的函数！"

if dump(a) :
    b(1)
else:
    print "a不是可调用的函数！"
