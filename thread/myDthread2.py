#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time,thread
#thread.start_new_thrad的用法
def timer():
	print "hello"
def test():
	for i in range(0,10):
		thread.start_new_thread(timer,())

if __name__=="__main__":
	test()
	time.sleep(10)
