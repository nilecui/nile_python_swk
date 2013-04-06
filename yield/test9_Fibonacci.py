#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2012-12-06 13:38
#       Filename: test9_Fibonacci.py
#    Description:
#****************************************************

# --------------------------------------------------------------------------
# @Synopsis  fab 递归数列
#
# @Param max
#
# @Returns
# --------------------------------------------------------------------------
#问题一
#fab函数中用print打印数字该函数复用性较差，因为fab返回None，其他函数无法获得
#该函数生成的队列
def fab(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1

#问题一解决方法
def fabList(max):
    n,a,b=0,0,1
    L=[]
    while n<max:
        L.append(b)
        a,b=b,a+b
        n=n+1
    return L

fab(5)
list=fabList(5)
for n in list:
    print n

#问题二：
#上面函数在运行中占用的内存会随着参数max的增大而增大，
#如果控制内存占用不要考虑List,通过iterable对象来迭代

#下面代码会生成1000个元素的List
for n in range(1000):
    pass

#不会生成1000元素的List，而是在每次迭代中返回一个数值，内存占用很小
#因为xrange不返回List,而返回一个iterable对象
for n in xrange(1000):
    pass


class Fab_Iterable(object):
    def __init__(self,max):
        print "__init__"
        self.max=max
        self.n,self.a,self.b=0,0,1

    def __iter__(self):
        print "__iter__"
        return self

    def next(self):
        print "next"
        if self.n<self.max:
            r=self.b
            self.a,self.b=self.b,self.a+self.b
            self.n=self.n+1
            return r
        raise StopIteration()
print "*"*30
#Fab_Iterable类通过next()不断返回数列的下一个数，内存占用始终为常数
for n in Fab_Iterable(5):
    print n


print "*"*30
#上面是不是太复杂些的，这个时候yield就出山了

def Fab_Yield(max):
    n,a,b=0,0,1
    while n<max:
        yield b #这里会中断
        a,b=b,a+b
        n=n+1

for n in Fab_Yield(5):
    print n


#yield的作用就是把一个函数变成一个generate，带有yield的函数不再是一个普通函数，python
#解释器会视为一个generate,调用函数后不会执行Fab_Yield函数，而是返回一个iterable对象
#在for循环执行时，每次循环都会执行Fab_Yield内部代码
#执行到yield b时,fab函数会返回一个迭代值，下次迭代时，从yield b的下一条语句执行




#判断一个函数是否是一个特殊的generate函数
#inspect 检查
from inspect import isgeneratorfunction

b=isgeneratorfunction(Fab_Yield)
print "b=",b


#yield 文件读取

def read_file(fpath):
    BLOCK_SIZE=1024
    with open(fath,'rb') as f:
        while True:
            block=f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
