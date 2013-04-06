#!/usr/bin/python
#-*- coding:utf-8 -*-


def say():
    print "hello"
    yield 5
    print "world"
y=say()

y.next()#这里会调用yield之前的东西
print "say 函数中没有yield======="
y.next()#因为函数内没有yield了，等着报错吧

