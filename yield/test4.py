#!/usr/bin/python
#-*- coding:utf-8 -*-


def h():
    print "one"
    yield 1
    print "two"
    yield 2
    print "three"
    yield 3

for i in h():
    print i
