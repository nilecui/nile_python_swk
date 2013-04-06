#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-04-03 13:37
#       Filename: simple_test1.py
#    Description:
#****************************************************

import urllib
from sgmllib import SGMLParser
import urlparse

class URLLister(SGMLParser):
    '''获取网页中所有链接地址,加入到列表中'''
    def reset(self):
        print "reset---->"
        self.urls = []
        SGMLParser.reset(self)

    #def start_a(self, attrs):
        #"""在序列中取出URL地址"""
        #print "start_a---->"
        #print attrs
        #urlList = [v for k, v in attrs if k=='href']
        #if urlList:
            #self.urls.extend(urlList)

    def start_dl(self, attrs):
        """在序列中取出URL地址"""
        #print "start_a---->"
        print attrs
        urlList = [v for k, v in attrs if k=='class']
        if urlList:
            self.urls.extend(urlList)

    def getHTML(self,targetUrl):
        """获取网页内容"""
        print "getHTML---->"
        sockPage=urllib.urlopen(targetUrl)
        HTML=sockPage.read()
        sockPage.close()
        return HTML


def getUrls (targetUrl):
    """获取URL地址后处理返回"""
    print "getUrls---->"
    parser = URLLister();
    HTML=parser.getHTML(targetUrl);
    print HTML
    parser.feed(HTML);# 装填分析器，使得"start_"开头的方法都被执行了
                      # 并自动匹配出所有已定义的start_方法的 tag 信息
    urlList = parser.urls
    parser.close()
    urlTup = urlparse.urlparse(targetUrl) #解析URL
    for i in range(len(urlList)):
        urlList[i] = addHttp(urlList[i],urlTup)
    return urlList

def addHttp(url,urlTup):
    """处理成完整的URL"""
    #print "addHttp---->"
    if url.startswith("http"):
        return url
    rootUrl = urlTup.scheme + "://" + urlTup.netloc
    if url.startswith("/"):
        fullUrl = rootUrl + url
    else:
        fullUrl = rootUrl + urlTup.path
    return fullUrl

if __name__ == "__main__":
    targetUrl = "http://data.ent.sina.com.cn/star/index.html?&tpl=0&dpc=1"
    urls = getUrls(targetUrl)
    for url in urls:
        print url
    print len(urls)
