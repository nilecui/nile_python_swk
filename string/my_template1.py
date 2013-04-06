#!/usr/bin/python
#-*- coding:utf-8 -*-
import string

values={'var':'foo'}
t=string.Template("""
        Variable:$var
        Escape:$$
        Variable in text:${var}iable
        """)
print "Template:",t.substitute(values)

s="""
    Variable:%(var)s
    Escape:%%
    Variable in text:%(var)siable
    """
print "Interpolation:",s % values
