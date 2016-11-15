#Lab 7 Hashes & Macs
#Author: Fionn Mcguire
#Student Number: C13316356
#Date: 14/11/2016

#Q1 Hashes

from pyDes import *
import base64

def addPadding(msg):
        length = 8-(len(msg)%8)
        i=0
        while(i<length):
                msg +="\x00"
                i+=1
        return msg

def removePadding(msg):
        str1 = "\x00"
        position = msg.find(str1,0)
        msg = msg[:position]
        return msg

def chunks(longdata,n):
    for i in range(0,len(longdata),n):
        yield longdata[i:i + n]
iv = '00000000'
plaintext = "AAAABBBBCCCCD"
plaintext = addPadding(plaintext)
datasource = dict(enumerate(list(chunks(plaintext,8)), start=1))
for d in datasource:
    k = des(datasource[d], 'ECB')
    encrypted = k.encrypt(iv)
    iv = "".join(chr(ord(x) ^ ord(y)) for x,y in zip(iv, encrypted))
print "Plaintext: "+plaintext
print "hash :" + str(map("".join,zip(*[iter(base64.b16encode(iv))]*16)))

#Q2 Mac


import hashlib
import hmac

mac_function = hmac.new('12345678')
plaintext = 'AAAABBBBCCCCD'
plaintext = addPadding(plaintext)
mac_function.update(plaintext)
hash_value = mac_function.hexdigest()
print hash_value









