#!/usr/bin/python
#-*- coding:utf-8 -*-
import string

template_text='''
Delimiter:%%
Replaced:%with_underscore
Ignored:%notunderscored
test:%test_test
test1:%testnot
'''



d={'with_underscore':'replaced',
'notunderscored':'not replaced',
'test_test':'for test ok!',
'testnot':'not test!',}

class MyTemplate(string.Template):
    delimiter='##'

def _test():
    s="##who likes ##what"
    t=MyTemplate(s)
    d={'who':'yaoming','what':'mac'}
    print t.substitute(d)
    print MyTemplate.delimiter
    print string.Template.delimiter

if __name__=='__main__':
    _test()
