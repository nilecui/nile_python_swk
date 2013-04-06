#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-29 17:01
#       Filename: xmltree.py
#    Description:
#****************************************************

from xml.etree import ElementTree

def print_node(node):
    print "====================================="

    print node.text
    for key,value in node.items():
        print "%s:%s" % (key, value)

    #for key,value in node.items():
      #print "%s:%s" % (key, value)
    for subnode in node.getchildren():
        print "%s:%s" % (subnode.tag, subnode.text)

def filter_result(node):
    seqlist=[]
    res=''
    for subnode in node.getchildren():
        print subnode.tag
        if subnode.tag=='rcode':
            res=subnode.text
        elif subnode.tag=='serverid':
            seqlist.append(subnode.text)

    return seqlist,res


def read_xml(text = '', xmlfile = ''):
    #root = ElementTree.parse(xmlfile)
    #tree=ElementTree.ElementTree()
    #tree.fromstring(text)
    root = ElementTree.fromstring(text)

    # 1 getiterator([tag=None])
    # only elements whose tag equals tag are returned from the iterator
    #eitor = root.getiterator("age")
    #for e in eitor:
        #print_node(e)

    # 2 getchildren()
    # Returns all subelements
    #eles_Paramter = root.find("message").findall("serverid")
    eles_Paramter = root.findall("serverid")
    print "111111111111111111111"
    print eles_Paramter
    for i in eles_Paramter:
        print_node(i)


    eitor = root.getchildren()
    print "eitor:",eitor
    for e in eitor:
        l,s=filter_result(e)
        print l,s
    print l,s


    #iiter=tree.iter('rcode')
    #for i in iiter:
        #print i.text


    # 3 findall(match)
    # Finds all subelements matching match.
    # match may be a tag name or path. Returns an iterable yielding all matching elements
    node_findall = root.findall("RESPONSE")
    print "node_findall:",node_findall
    for e in node_findall:
        print_node(e)

    # 4 find(match)
    # Finds the first subelement matching match.
    # match may be a tag name or path. Returns an element instance or None
    node_find = root.find('rcode')
    print_node(node_find)
    print node_find.text

    node_find=root.find('serverid')
    print "----"
    print node_find


    #iter=root.get('rcode')
    #print iter.text


if __name__ == '__main__':
    xmlstr='<?xml version="1.0" encoding="UTF-8"?><RESPONSE><rcode>00</rcode><message><destmobile>13601192499</destmobile><serverid>237</serverid><destmobile>13601192499</destmobile><serverid>235</serverid><destmobile>13601192499</destmobile><serverid>233</serverid></message></RESPONSE>'
    #read_xml(open("./phone.xml").read())
    read_xml(xmlstr)
