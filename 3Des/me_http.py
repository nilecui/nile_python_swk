#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-22 17:15
#       Filename: http.py
#    Description:
#****************************************************
from Crypto.Cipher import DES3
import base64
import binascii
#import binascii import unhexlify as unhex
from pyDes import *
import pyDes

from binascii import hexlify
from binascii import unhexlify
from base64 import *


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


KEY="LTSMS4569856432146890865"
IV='12345678'
#_3DES = pyDes.triple_des('LTSMS4569856432146890865', pyDes.CBC, '12345678', pad = None, padmode = pyDes.PAD_PKCS5)
#IV= binascii.unhexlify("12345678")
print "IV=",IV
_3DES = pyDes.triple_des('LTSMS4569856432146890865'.encode('utf-8'), pyDes.CBC,IV='12345678', pad = None, padmode = pyDes.PAD_PKCS5)
#_3DES = pyDes.triple_des('LTSMS4569856432146890865'.encode('utf-8'), pyDes.CBC,IV='\0\0\b\c\6\1\4\e', pad = None, padmode = pyDes.PAD_PKCS5)
#_3DES = pyDes.triple_des('LTSMS4569856432146890865'.encode('utf-8'), pyDes.CBC,IV=12345678, pad = None, padmode = pyDes.PAD_PKCS5)
#_3DES = pyDes.triple_des('LTSMS4569856432146890865', pyDes.CBC,IV="12345678")

def Encrypt(data):
    e = _3DES.encrypt(data.encode('utf-8'))
    return base64.b64encode(e)

def Decrypt(enData):
    d = base64.b64decode(enData)
    return _3DES.decrypt(d)

class MEncrypter(object):

    def __init__(self, key):
        if len(key) < 24:
            key = key + b64encode(key.encode("utf-8"))
            key = key + b64encode(key.encode("utf-8")) * 2

        key = key[0:24]

        self.k = pyDes.triple_des(key.encode("utf-8"), CBC, "12345678", pad=None, padmode=PAD_PKCS5)

    def encrypt(self, text):
        return hexlify(self.k.encrypt(text.encode("utf-8")))

    def decrypt(self, text):
        return unicode(self.k.decrypt(unhexlify(text)),"utf-8")



def PKCS5Pading(src):
    lent=8-len(src)%8
    if lent==0 or lent==8:
        padstring='\x08\x08\x08\x08\x08\x08\x08\x08'
    if lent==7:
        padstring='\x07\x07\x07\x07\x07\x07\x07'
    if lent==6:
        padstring='\x06\x06\x06\x06\x06\x06'
    if lent==5:
        padstring='\x05\x05\x05\x05\x05'
    if lent==4:
        padstring='\x04\x04\x04\x04'
    if lent==3:
        padstring='\x03\x03\x03'
    if lent==2:
        padstring='\x02\x02'
    if lent==1:
        padstring='\x01'
    des=src+padstring
    return des

def EncryDES3(src):   #DES3加密

    objstr=PKCS5Pading(src)
    obj = DES3.new(KEY,DES3.MODE_CBC,IV)
    return obj.encrypt(objstr)

def DecryDES3(src):#DES3解密
    #if len(src)%8!=0:
        #return ''
    #d = base64.b64decode(src)
    #d = base64.urlsafe_b64decode(src)
    print "src:",src
    d = base64.standard_b64decode(src)
    print "d:",d

    obj = DES3.new(KEY,DES3.MODE_CBC,IV)
    des=obj.decrypt(d)
    length=ord(des[-1:])
    if des[-length:]!=des[-1:]*length:
        return ''
    else:
        return des[:-length]



if __name__ == '__main__':

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

    en_msg=Encrypt(o_msg)
    print "en_msg:",en_msg

    en_data={'operid':OperID,\
        'operpass':OperPass,\
        'en3des':en_msg}

    xmlstr = xml_mt(**en_data)
    print xmlstr

    de_msg=Decrypt(en_msg)
    print "de_msg:",de_msg

    #de_tstr=Decrypt(tstr)
    #print "de_tstr:",de_tstr

    r,s,t=do_http('123.125.199.164:9280','/leadtone/Sms/Submit', 'POST', xmlstr)
    print r,s,t
    #print "sx:",binascii.unhexlify(s)
    #res=Decrypt(s)
    enen="HQna/TtkMJkNW7A/qzhpcjc5poch0HAhrA5/AIKimuvgmzuurUrkWoXyTkpyRXbpY3oW10lbTFeS"
    res=DecryDES3(enen)
    print "res:",res


    #enc = MEncrypter('LTSMS4569856432146890865')
    #e=enc.encrypt(o_msg)
    #print e
