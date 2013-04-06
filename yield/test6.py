#!/usr/bin/python
#-*- coding:utf-8 -*-


def h():
    print "-"*20
    while True:
        print "#"*10
        x=yield
        print x
        print "%"*10

y=h()
print y

y.next()
y.next()
y.next()

y.send('hellow world')
