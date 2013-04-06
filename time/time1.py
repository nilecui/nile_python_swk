#!/usr/bin/python
#-*- coding:utf-8 -*-

import datetime
import time

#now=datetime.datetime.now()
now=time.localtime(time.time())

dateF=time.strftime("%Y%m%d%H%M%S",now)

print dateF

print now
