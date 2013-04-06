#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-15 15:27
#       Filename: sax_test.py
#    Description:
#****************************************************

import sys
from xml.sax import parse,make_parser,parseString,handler,SAXException

xmlString='<img src="a.jpg" alt="a.jpg" width="100" height="200">hello</img>'

class MyHandler(handler.ContentHandler):
    """用户自定义事件处理器"""

    def __init__(self,start_e,end_e,gkey_elist,gkey_attrlist):
        self.get_clist=gkey_elist
        self.get_alist=gkey_attrlist
        #self.get_alist.extend(self.get_clist)
        self.tlist=self.get_alist+self.get_clist
        self.start_e=start_e
        self.end_e=end_e
        self.elelist=[]
        self.eledict={}
        self.flag=None

    def get_data(self):
        return self.elelist

    def startDocument(self):
        print "Doc Start..."

    def endDocument(self):
        print "Doc End..."

    def startElement(self,element,attrs):

        attrs_list=dict(attrs)
        print "attrs_list:",attrs_list
        if element == self.start_e:
            #首先对初始标签初始化
            self.eledict={}.fromkeys(self.tlist,'')
            #匹配属性值
            for s in attrs_list:
                for k in self.get_alist:
                    if s==k:
                        self.eledict[s]=attrs_list[s]
        else:
            #非根节点数据处理:
            for s in self.get_clist:
                if s==element:
                    #数据只能依次加入列表,因为调用characters属于事件驱动
                    #设置标志位，获得内容后清除
                    self.flage=s


        print "self.eledict:",self.eledict

    def endElement(self,end_ele):
        #初始化数据
        print "endElement..."
        #判断表示位是否为空
        #判断是否为最后一个字符
        if end_ele == self.start_e:



    def characters(self,content):
        if content.isspace():
            return

        if self.flag is not None:
            self.elelist.append(content)

        print "characters:"+content

#解析xml文件
#try:
    #parse('./stu.xml',MyHandler())
#except SAXException,msg:
    #print msg.getException()
#except:
    #print sys.exc_info()[0],sys.exc_info()[1]


解析xml字符串
#print "Test parseString---->"
#try:
    #parseObj=parseString(xmlString,MyHandler())
#except SAXException,msg:
    #print msg.getException()
#except:
    #print sys.exc_info()[0],sys.exc_info()[1]


if __name__=='__main__':

    try:
        start='student'
        end='student'
        klist=['name','age','dob']
        attlist=['id']

        objHander=MyHandler(start,end,klist,attlist)
        parse('./stu.xml',objHander)
    except SAXException,msg:
        print msg.getException()
    except:
        print sys.exc_info()[0],sys.exc_info()[1]
