#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import string

def replace(file,search_for,replace_with):

    print "file name:",os.path.splitext(file)[0]

    back=os.path.splitext(file)[0]+".bak"
    temp=os.path.splitext(file)[0]+".temp"

    try:
        os.remove(temp)
    except os.error:
        pass

    fi=open(file)
    fo=open(temp,"w")

    for s in fi.readlines():
        fo.write(string.replace(s,search_for,replace_with))

    fi.close()
    fo.close()

    try:
        os.remove(back)
    except os.error:
        pass

    os.rename(file,back)
    os.rename(temp,file)

file="hello.txt"

replace(file,"hello","nononono")
replace(file,"beijing","yesyesyes")
replace(file,"日本","小日本")
