#!/usr/bin/python
#-*- coding:utf-8 -*-


def h():
    print "wen chuan..."
    m=yield 5#Fighting
    print m
    d=yield 12
    print 'we are together!'

c=h()
c.next()#相当于c.send(None)

c.send('Fighting!')
