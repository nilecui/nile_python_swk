#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time,thread
#thread.start_new_thrad的用法
def timer(no,interval):
	cnt=0
	while cnt<4:
		print "Thread:(%d) Time:%s\n"%(no,time.ctime())
		time.sleep(interval)
		cnt+=1
	#线程的结束
	#1、可以等待线程自然借宿
	#2、可以调用thread.exit()或thread.exit_thread()结束
	thread.exit_thread()

def test():
	#for i in range(0,2):
	thread.start_new_thread(timer,(1,1))
	#thread.start_new_thread(timer,(2,2))


if __name__=="__main__":
	test()
	time.sleep(10)
