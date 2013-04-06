#!/usr/bin/python
#-*- coding:utf-8 -*-
#http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#Quick%20Start
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

#获得title标签和内容
titleTag=soup.html.head.title
print "titleTag---->",titleTag

#获得title标签内容
ctitle=titleTag.string
print "ctitle---->",ctitle

#查询有多少个
totalp=len(soup('p'))
print "totalp---->",totalp

#findAll查询特定标签,返回列表
fa_pcontent=soup.findAll('p',align="center")
print "fa_pcontent---->",fa_pcontent

#find查询特定标签,注意findAll和find返回结果,返回字符串
f_pcontent=soup.find('p',align="center")
print "f_pcontent---->",f_pcontent

#获得标签内某字段的属性
id_attr=soup('p',align="center")[0]['id']
print "soup('p',align='center')[0]---->",soup('p',align="center")[0]
print "id_attr---->",id_attr

#find内正则模糊匹配查找
p_f_re=soup.find('p',align=re.compile('^b.*'))['id']
print "soup.find('p',align=re.compile('^b.*'))---->",soup.find('p',align=re.compile('^b.*'))
print "p_f_re---->",p_f_re

#find方法查找p标签后获得b标签查询和内容
f_b_con=soup.find('p').b.string
print "soup.find('p').b---->",soup.find('p').b
print "f_b_con---->",f_b_con

#soup直接获得b标签和内容
s_b_con=soup('p')[1].b.string
print "soup('p')---->",soup('p')
print "soup('p')[1].b---->",soup('p')[1].b
print "s_b_con---->",s_b_con

