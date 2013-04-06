#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

#获取某目录中的文件及子目录的列表
#使用os.listdir搜索文件系统
def index(directory):
    stack=[directory]
    print "stack=",stack
    files=[]

    while stack:
        directory=stack.pop()
        print "directory=",directory
        for file in os.listdir(directory):
            fullname=os.path.join(directory,file)
            print "fullname=",fullname
            files.append(fullname)
            #判断路径是否是目录
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files

for file in index("../"):
    print file
