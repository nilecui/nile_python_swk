#!/usr/bin/python
#-*- coding:utf-8 -*-

l=[12,9,1,3,0]
print "l=",l

print "排序后:"
l.sort()
print l

def my_cmp(e1,e2):
    print "e1=",e1
    print "e2=",e2
    return -cmp(e1[1],e2[1])

l=[('a',0),('b',1),('c',2),('d',3)]
print l
l.sort(my_cmp)
print l


from random import shuffle

def my_cmp1(e1,e2):
    print "e1=",e1,"e2=",e2
    return cmp(e1,e2)
#二分插入排序
l=range(0,10)
shuffle(l)
print l
l.sort(my_cmp1)
print l


#看看一个排序好的数组
l=[0,1,2,3,4,5,6,7,8,9,10]
l.sort(my_cmp1)
print "*************************************"
l=[0,2,1,3,4,5,6,7,8,9,10]
l.sort(my_cmp1)
#sort采用的是混合（hybrid）排序，规模小的时候采用binary insertion，规模大的时候采用samplesort
