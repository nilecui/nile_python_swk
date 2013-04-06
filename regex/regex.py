#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys

def calc(str):
    import re
    num=re.compile('\d+')
    opr=re.compile('[+\-*/()]')

    i=num.match(str)
    if i:
        print "i=",i,
        #返回被re匹配的字符串
        print "i.group()=",i.group()

        #返回匹配开始的位置
        print "i.start()=",i.start()

        #返回匹配结束的位置
        print "i.end()=",i.end()

        #返回一个元组包含匹配(开始，结束)的位置
        print "i.span()=",i.span()

    else:
        print "i=",i,
    j=opr.match(str)

    if j:
        print "j=",j,
        #返回被re匹配的字符串
        print "j.group()=",j.group()

        #返回匹配开始的位置
        print "j.start()=",j.start()

        #返回匹配结束的位置
        print "j.end()=",j.end()

        #返回一个元组包含匹配(开始，结束)的位置
        print "j.span()=",j.span()
    else:
        print "j=",j,

print sys.argv[0]
print sys.argv[1]
#print os.system(sys.argv[])

calc(sys.argv[1]);
