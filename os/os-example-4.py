#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

cwd=os.getcwd()
print "1",cwd

os.chdir("samples")
print "2",os.getcwd()

os.chdir(os.pardir)
print "3",os.getcwd()
