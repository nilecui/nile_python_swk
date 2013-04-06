#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-04-03 09:53
#       Filename: bs_test1.py
#    Description:
#****************************************************

from BeautifulSoup import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

#print "soup.prettify---->",soup.prettify()


print "soup.contents---->",soup.contents
print "soup.contents[0]---->",soup.contents[0]
print "soup.contents[0].name---->",soup.contents[0].name

head=soup.contents[0].contents[0]
print "head---->",head
print "soup.contents[0].contents[0]---->",soup.contents[0].contents[0]
print "soup.contents[0].contents[0].name---->",soup.contents[0].contents[0].name

print "head.next---->",head.next

#获得兄弟标签
print "head.nextSibling---->",head.nextSibling
sibling_tag=head.nextSibling.name
print "sibling_tag--->",sibling_tag

#获得body内的内容
cbody=head.nextSibling.contents
print "cbody---->",cbody

for p in cbody:
    print "p--->",p

