#!/usr/bin/python
#-*- coding:utf-8 -*-

from Queue import Queue

#Queue.Queue类即是一个队列的同步实现
#队列的长度可为无线或者有限
#而通过Queue的构造函数的可选参数maxsize来设定队列长度
#如果maxsize小于1表示队列长度无线
myqueue=Queue(maxsize=10)

#将一个值放入队列中
#put()方法有两个参数
#第一个item为必须的，为插入项目的值
#第二个block为可选参数，默认为1
#如果队列当前为空，且block为1，put方法就调用线程暂停，直到空出一个数据单元
#如果block为0，put方法引发Full异常
myqueue.put((10,9))

print "queue size=",myqueue.qsize()#返回队列的大小
print "queue data=",myqueue.get()#获得队列
print "queue is empty?",myqueue.empty()#如果队列为空，返回True,反之False
print "queue is full?",myqueue.full()#如果队列满了，返回True,反之False
#print "queue get_nowait=",myqueue.get_nowait()#相当Queue.get(False),
#非阻塞Queue.put(item)写入队列，timeout等待时间

#print "queue put_nowait=",myqueue.put_nowait()#相当Queue.put(item.False),

print "queue task_done=",myqueue.task_done()#在完成一项工作之后
#task_done函数向已经完成的队列发送一个信号

#join()实际上是意味着等到队列为空，再执行别的操作
