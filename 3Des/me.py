#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-22 17:15
#       Filename: http.py
#    Description:
#****************************************************
import binascii
import base64
from Crypto.Cipher import DES3

#密钥
#KEY = binascii.a2b_hex('CEC801199468CB678C1A983131628F20F1165BBFE5FD7310') #调用BinAscii模块其中的b2a_hex()函数，可把以ASCII编码的密钥以十六进制表示：
KEY = 'LTSMS4569856432146890865'
#IV = binascii.a2b_hex('12345678')  #IV向量值
IV = '12345678'  #IV向量值

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
    #return obj.encrypt(objstr)
    s1=obj.encrypt(objstr)
    return base64.b64encode(s1)

def DecryDES3(src):#DES3解密
    #if len(src)%8!=0:
        #return ''
    #s=base64.b64decode(src)
    s=base64.decodestring(src.replace('\n',''))
    obj = DES3.new(KEY,DES3.MODE_CBC,IV)
    des=obj.decrypt(s)
    length=ord(des[-1:])
    if des[-length:]!=des[-1:]*length:
        return ''
    else:
        return des[:-length]


if __name__=="__main__":
    data='<?xml version="1.0" encoding="UTF-8"?><RESPONSE><rcode>05</rcode></RESPONSE>'

    en_str=EncryDES3(data)
    print en_str

    en_str="HQna/TtkMJkNW7A/qzhpcjc5poch0HAhrA5/AIKimuvgmzuurUrkWoXyTkpyRXbpY3oW10lbTFeSVhMOtPdMyFZ6jfMFsP4KVMfq5kzQ/1M="
    de_str=DecryDES3(en_str)
    print de_str
