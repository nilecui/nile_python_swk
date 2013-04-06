#!/usr/bin/python2.6
#-*- coding:utf-8 -*-

import re

p=re.compile("...")
m=p.match('string goes here')
if m:
    print "match found:",m.group()
else:
    print "No matchch"
