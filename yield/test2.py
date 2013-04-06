#!/usr/bin/python
#-*- coding:utf-8 -*-


#在python2.5以前是一个语句，现在是一个表达式
def h():
    print "to be brave"
    yield 5
h()


#m=yield 5
#如何获得m的值呢,需要了解send(msg)方法


#生产出来了不用，浪费资源,如何用呢？
def h1():
    print 'Wen Chuan'
    yield 5
    print 'Fighting'

c=h1()
c.next()
c.next()

