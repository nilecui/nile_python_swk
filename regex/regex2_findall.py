#!/usr/bin/python
#-*- coding:utf-8 -*-
import re

p=re.compile('\d+')
l=p.findall('12 drummers drumming,11 pipers piping,10 lords a-leaping')
print l
