#!/usr/bin/python
#-*- coding:utf-8 -*-
import os

def callback(arg,directory,files):
    print "arg=",arg
    print "directory=",directory
    print "files=",files

    for file in files:
        print os.path.join(directory,file),repr(arg)

os.path.walk("../",callback,"secret msg...")
