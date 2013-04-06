#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-22 10:24
#       Filename: 3des_test.py
#    Description:
#****************************************************


import pyDes
import base64

_3DES = pyDes.triple_des('LTSMS4569856432146890865', pyDes.CBC, '01234567', pad = None, padmode = pyDes.PAD_PKCS5)

def Encrypt(data):
    e = _3DES.encrypt(data)
    return base64.b64encode(e)

def Decrypt(enData):
    d = base64.b64decode(enData)
    return _3DES.decrypt(d)

if __name__=="__main__":
    str1="中国"
    en_str=Encrypt(str1)
    print en_str

    de_str=Decrypt(en_str)
    print de_str
