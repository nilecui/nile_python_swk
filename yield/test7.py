#!/usr/bin/python
#-*- coding:utf-8 -*-


def say():
    print "hello\n",
    m=yield 5

    print m
    d=yield 12

    print "world"
    print d
    yield 1

p=say()
print "->"*10
p.next()
print "->"*10

print p.send("world!")
print "->"*10

p.next()
print "->"*10

p.next()
