#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-04-02 14:24
#       Filename: soaptest.py
#    Description:
#****************************************************



#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

html_doc="""
<html><head><title>The Dormouse's story中国</title></head>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>"""

print isinstance(html_doc,unicode)
#utf-8 转化为unicode
unicodehtm=html_doc.decode('utf-8','ignore')
print unicodehtm

soup=BeautifulSoup(''.join(html_doc))
#soup=BeautifulSoup(''.join(unicodehtm))
print "soup--->",soup
print "soup.title--->",soup.title

print "soup.pretty--->",soup.prettify()

