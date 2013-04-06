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

titleTag=soup.html.head.title
print titleTag
#替换标题，并且添加id标签
titleTag['id']='the Title'
titleTag.contents[0].replaceWith("New title")
print soup.html.head

#提取p标签内容
extract_html=soup.p.extract()
print "extract_html---->",extract_html

#修饰
prettify_html=soup.prettify()
print "prettify_html---->",prettify_html

#修改标签b
mod_p=soup.p.replaceWith(soup.b)
print "mod_p---->",mod_p
print "replace soup---->",soup

#body标签内插入数据
soup.body.insert(0,"This page used to have!")
soup.body.insert(2,"&lt;p&gt;tags!")
print soup.body
