#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-29 17:16
#       Filename: str_test.py
#    Description:
#****************************************************



xml="<s1>1212</s1><t1>2121</t1><s1>1313</s1><t1>2121</t1><s1>1313</s1><t1>2121</t1><s1>1313</s1>"

start=0
seqids=[]
data_tail=xml
print data_tail

#while (start!=-1):
    #tlen=len("<s1>")
    #print "tlen:",tlen
    #start=data_tail.find('<s1>')+tlen
    #print "start:",start
    #end=data_tail.find('</s1>')
    #print "end:",end
    #seqid=data_tail[start:end]
    #print "seqid:",seqid
    #seqids.append(seqid)
    #data_tail=data_tail[end:]

print "seqids:",seqids

