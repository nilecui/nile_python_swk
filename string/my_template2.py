#!/usr/bin/python
#-*- coding:utf-8 -*-
import string

values={'var':'foo'}
#values={'var':'foo','missing':'good'}
t=string.Template("$var is here but $missing is not provided!")
try:
    print 'substituteb():',t.substitute(values)
except KeyError,err:
    print 'ERROR:',str(err)
print 'safe_substitute():',t.safe_substitute(values)
