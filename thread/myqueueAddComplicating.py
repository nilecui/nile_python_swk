#!/usr/bin/python
#-*- coding:utf-8 -*-

import threading
import subprocess
import Queue
import time

num_thread=10 #线程数
queue=Queue.Queue()#队列实例化

ips=["www.baidu.com","www.google.com","www.360buy.com","www.taobao.com"]
def pinger(i,q):
	while True:
		ip=q.get()
		print "Thread %s:Ping %s\n"%(i,ip)
		ret=subprocess.call("ping -c 1 %s"%ip,
							shell=True,
							stdout=open('/dev/null','w'),
							stderr=subprocess.STDOUT)
		if ret==0:
			print "%s :is alive!\n"%ip
		else:
			print "%s :did not respond!\n"%ip
		q.task_done()#告诉queue.join已经完成从队列中提取元素的工作

#创建num_thread个线程
for i in range(num_thread):
	work=threading.Thread(target=pinger,args=(i,queue))
	work.setDaemon(True)#设置子进程是否随主进程一起结束
	work.start()
for ip in ips:
	print "Put date to Queue...\n"
	queue.put(ip)#将ip放入队列中

print "Main Thread Waiting...\n"
queue.join()
print "Done...\n"
