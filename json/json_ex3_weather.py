#!/usr/bin/python
#-*- coding:utf-8 -*-

import httplib
import simplejson as json

conn=httplib.HTTPConnection("m.weather.com.cn")
conn.request("GET","/data/101100101.html")
weather=conn.getresponse()
info=weather.read()
print info
weatherinfo=json.loads(info)
print weatherinfo['weatherinfo']['city'],
conn.close()
