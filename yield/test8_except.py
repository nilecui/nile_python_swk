#!/usr/bin/python
#-*- coding:utf-8 -*-


def echo(value=None):
    print "Excution starts when next() is called for the first time."
    try:
        while True:
            try:
                value=(yield value)
            except Exception,e:
                value=3
    finally:
        print "Don't forget to clean up when 'close()'is called"


generator=echo(1)
print generator.next() #1
print generator.next() #None
print generator.send(2) #2 yield value
generator.throw(TypeError,"spam")
generator.close()
