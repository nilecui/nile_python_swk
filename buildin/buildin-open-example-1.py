#!/usr/bin/python
#-*- coding:utf-8 -*-

def open(filename,mode="rb"):
    import __builtin__
    file=__builtin__.open(filename,mode)
    if file.read(5) not in ("GIF87","GIF89"):
        raise IOError,"not a GIF file"
    file.seek(0)
    return file

fp=open("sample1.gif")
print len(fp.read()),"bytes"

fp=open("sample2.gif")
print len(fp.read()),"bytes"
