#!/usr/bin/python
#!-*- coding:utf-8 -*-

dict={'a':'hello','b':'world'}

print dict

new_dict=dict.copy();
print new_dict

print new_dict.has_key('a')


dict["c"]="ok"
print dict

dict.setdefault(2,'ok')
print dict
