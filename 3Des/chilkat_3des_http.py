#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-22 17:15
#       Filename: http.py
#    Description:
#****************************************************

import pyDes
import base64
import binascii
#import binascii import unhexlify as unhex
from pyDes import *

from binascii import hexlify
from binascii import unhexlify
from base64 import *
import chilkat
import sys


import simplejson
from twisted.web import resource, server
from httplib import HTTPConnection
from urllib import urlencode, unquote
import os
import time
from twisted.python import log
from twisted.internet import reactor , threads, task, protocol
#from datacenter.main import *
HTTP_TIMEOUT = 30
HTTP_POST = 'POST'
HTTP_GET = 'GET'
#HTTP_HEADERS = {'content-type':'text/plain'}
HTTP_HEADERS = {'Content-Type':'text/xml; charset=utf-8'}

_get_one = lambda (k, v):(k, v[0])

def parse_get_pramas(data):
    return dict(map(_get_one, data.items()))

def parse_qs(s):
    d = {}
    s = unquote(s)
    for item in s.split('&'):
        k, v = item.split("=", 1)
        d[k] = v
    return d




def do_http(host,url, method, params = None, headers = {}):

    '''发送HTTP请求'''

    try:
        if HTTP_GET == method and params:
            requrl = '%s?%s'%(url, urlencode(params))
        else:
            requrl = url
        req = HTTPConnection(host,timeout = HTTP_TIMEOUT)
        req.connect()
        if HTTP_POST == method:
            reqheaders = HTTP_HEADERS.copy()
            reqheaders.update(headers)
            req.request(method, requrl, params, reqheaders)
        else:
            req.request(method, requrl, '', headers)
        resp = req.getresponse()
        return resp.status, resp.read(), resp
    except:
        log.err()
        log.msg('发送HTTP请求失败=====>:', host, url)
        return None, None, None

def xml_mt(**kwargs):
        return '''<?xml version="1.0" encoding="UTF-8"?><ROOT><HEAD><OperID>%s</OperID><OperPass>%s</OperPass></HEAD><BODY>%s</BODY></ROOT>'''%(kwargs['operid'],kwargs['operpass'],kwargs['en3des'])

def xml_body(**kwargs):
        return '''<AppendID>%s</AppendID><DestMobile>%s</DestMobile><Content>%s</Content><ContentType>%s</ContentType>'''%(kwargs['port'],kwargs['phone'],kwargs['msg'],kwargs['type'])

crypt = chilkat.CkCrypt2()
success = crypt.UnlockComponent("Anything for 30-day trial")

if __name__ == '__main__':
    if (success != True):
        print crypt.lastErrorText()
        sys.exit()

    crypt.put_CryptAlgorithm("des")
    crypt.put_KeyLength(24)
    crypt.put_EncodingMode("base64")
    crypt.put_CipherMode("cbc")
    crypt.SetEncodedIV("12345678","hex")
    crypt.SetEncodedKey("LTSMS4569856432146890865","hex")
    crypt.put_PaddingScheme(4)

    OperID="testsms"
    OperPass="12345678A"
    msg="yzzx test"
    phone="13601192499"
    msg_type=15

    data={'port':'123',
            'phone':phone,
            'msg':msg,
            'type':msg_type}
    o_msg=xml_body(**data)
    print o_msg

    en_msg=crypt.encryptStringENC(o_msg)
    print "en_msg:",en_msg

    en_data={'operid':OperID,\
        'operpass':OperPass,\
        'en3des':en_msg}

    xmlstr = xml_mt(**en_data)
    print xmlstr

    de_msg=crypt.decryptStringENC(en_msg)
    print "de_msg:",de_msg

    #de_tstr=Decrypt(tstr)
    #print "de_tstr:",de_tstr

    r,s,t=do_http('123.125.199.164:9280','/leadtone/Sms/Submit', 'POST', xmlstr)
    print r,s,t

    CKString outs

    dec=crypt.DecodeString(s,"unicode",base64,outs)
    print "outs:",outs

    #res=crypt.decryptStringENC(outs)
    #print "res:",res


    #enc = MEncrypter('LTSMS4569856432146890865')
    #e=enc.encrypt(o_msg)
    #print e
