#!/usr/bin/python

execfile("hello.py")

def EXECFILE(filename,loacals=None,globals=None):
    exec compile(open(filename).read(),filename,"exec") in loacals,globals

EXECFILE("hello.py")
