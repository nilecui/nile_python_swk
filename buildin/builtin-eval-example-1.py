#!/usr/bin/python
#-*- coding:utf-8 -*-

def dump(expression):
    rs=eval(expression)
    print expression,"=>",rs,type(rs)

#转为整型
dump("1")
dump("1.0")

dump("'string'")
dump("1.0+2.0")

dump("'*'*10")
dump("len('world')")
