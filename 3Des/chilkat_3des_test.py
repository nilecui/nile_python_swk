#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-03-25 10:01
#       Filename: chilkat_3des_test.py
#    Description:
#****************************************************


import sys
import chilkat

crypt = chilkat.CkCrypt2()
success = crypt.UnlockComponent("Anything for 30-day trial")

if (success != True):
    print crypt.lastErrorText()
    sys.exit()

crypt.put_CryptAlgorithm("des")
crypt.put_KeyLength(24)
#crypt.put_EncodingMode("hex")
#crypt.put_EncodingMode("utf-8")
crypt.put_EncodingMode("base64")

crypt.put_CipherMode("cbc")
crypt.SetEncodedIV("12345678","hex")
crypt.SetEncodedKey("LTSMS4569856432146890865","hex")
crypt.put_PaddingScheme(4)
#cipherText = crypt.encryptStringENC("ABCDEFGHIJKLMNLPQRSTUVWXYZ")
cipherText = crypt.encryptStringENC("<AppendID>123</AppendID><DestMobile>13601192499</DestMobile><Content>宇宙之讯测试</Content><ContentType>15</ContentType>")
print cipherText
cipherText="HQna/TtkMJkNW7A/qzhpcjc5poch0HAhrA5/AIKimuvgmzuurUrkWoXyTkpyRXbpY3oW10lbTFeSVhMOtPdMyFZ6jfMFsP4KVMfq5kzQ/1M="
#str1=base64.b64decode(cipherText)
#plainText = crypt.decryptStringENC(64str1)
plainText = crypt.decryptStringENC(cipherText)
print plainText

