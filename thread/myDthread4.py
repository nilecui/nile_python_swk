#!/usr/bin/env python
#-*- coding:utf-8 -*-
import threading
import time

#run(),通常需要重写，编写代码实现需要做的功能
#getName(),获得线程对象名称
#setName(),设置线程对象名称
#start(),启动线程
#join([timeout]),等待另一线程结束后再运行
#setDeamon(bool),设置子线程是否随主线程一起结束，必须在start()之前调用，默认为False
#isDeamon,判断线程是否随主线程一起结束
#isAlive(),检查线程是否存在
class MyThread(threading.Thread):
	def __init__(self,num,interval,name=None):
		threading.Thread.__init__(self)
		self.name=name
		self.thread_num=num
		self.interval=interval
		self.thread_stop=False
	def run(self):
		while not self.thread_stop:
			print 'Thread Object (%d),name=(%s),time:(%s)' % (self.thread_num,self.name,time.ctime())
			time.sleep(self.interval)
	def stop(self):
		self.thread_stop=True

def test():
	thread1=MyThread(1,1,"a")
	thread2=MyThread(2,2,"b")

	thread1.start()
	thread2.start()

	time.sleep(20)
	thread1.stop()
	thread2.stop()
if __name__=="__main__":
	test()
