#!/usr/bin/env python
#coding=utf-8
import os,urllib2
from BeautifulSoup import BeautifulSoup
def getinfo(url):
    #检测url
    #略
    st = ''
    page = urllib2.urlopen(url)
    #soup = BeautifulSoup(page,fromEncoding="GBK")
    soup = BeautifulSoup(page)
    print soup

    #开始解析
    #info = soup.findAll('td',height="23",align="left")

    if ("class" in soup):
        print "class in soup!!!!"

    info = soup.findAll('div',{'class':'blank9'})
    print "info----->"
    #for i in info:
        #isinstance(i.strong.string, unicode) ，此函数用以判断字符串是否为unicode编码
        #print i.strong.string,getstring(i.strong.nextSibling)
        #st = st + str(i.strong.string)+str(getstring(i.strong.nextSibling))+'/n'

    fi = open("./123.txt",'w')
    #fi.write(st)
    fi.close()
def getstring(s):
    try:
        return s.string
    except:
        return s

if __name__=="__main__":
    url = "http://datalib.ent.qq.com/star/97/index.shtml"
    getinfo(url)
