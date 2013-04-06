#!/usr/bin/python
#-*- coding:utf-8 -*-

from xml.etree import ElementTree

def print_node(node):
    '''打印节点信息'''
    print "="*30
    print "node.attrib:%s"%node.attrib
    if node.attrib.has_key("age")>0:
        print "node.attrib['age']:%s"%node.attrib['age']
    print "node.tag:%s"%node.tag
    print "node.text:%s"%node.text

def read_xml(text):
    '''读取xml文件'''
    #加载xml文件（2种方法，一是加载指定字符串，二是加载指定文件）
    #root=ElementTree.parse(r"./test.xml")
    root=ElementTree.fromstring(text)

    #获取element的方法
    #1 通过getiterator
    print "*"*10+"方法一"+"*"*10
    lst_node=root.getiterator("person")
    for node in lst_node:
        print_node(node)


    #2 通过getchildren
    print "*"*10+"方法二"+"*"*10
    lst_node_child=lst_node[0].getchildren()[0]
    print_node(lst_node_child)

    #3 find方法
    print "*"*10+"方法三"+"*"*10
    node_find=root.find("person")
    print_node(node_find)

    #4 findall方法
    print "*"*10+"方法四"+"*"*10
    node_findall=root.findall("person/name")[1]
    print_node(node_findall)


def read_xml1(text):
    i=0
    print "read_xml1--->",text
    root=ElementTree.fromstring(text)
    res=root.findall("person/name")[i]
    print "res=",res
    print_node(res)

    print "res=",res
    while res is not 0:
        print "while--->"
        res=root.findall("person/name")[i]
        i+=1
        print_node(res)

def read_xml_for(text):
    tree=ElementTree.parse("test.xml");
    print tree;

    root=tree.getroot()

    for x in root:
        print x
        print x.findall("person");


if __name__=='__main__':
    read_xml(open("test.xml").read())
    #read_xml1(open("test.xml").read())
    #read_xml_for(open("test.xml").read())

