#!/usr/bin/python
#-*- coding:utf-8

import ThreadPool
import time,random

def hello(str):
    time.sleep(2)
    return str+"over!"

def print_res(request,result):
    print "the result is %s %r" % (request.requestID,result)

data=[random.randint(1,10) for i in range(20)]

pool=threadpool.ThreadPool(5)

requests=threadpool.makeRequests(hello,data,print_res)
[pool.putRequest(req) for req in requests]
pool.wait()
