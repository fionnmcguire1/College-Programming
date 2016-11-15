#-*- coding: utf-8 -*-
'''
C13316356
Fionn Mcguire
Advanced Security
Lab 3
DES with ECB mode encryption & Decryption
'''
	

#importing the encrytption algorithm
from pyDes import *
import base64

#Q1

'''
Key      : '12345678'
Plaintext     : AAAABBBBAAAABBBB
Encrypted: '\x19\xffF7\xbb/\xe7|\x19\xffF7\xbb/\xe7|'

Ciphertext     : 19FF4637BB2FE77C19FF4637BB2FE77C
Decrypted     : '9\x07\xa6\xc1\xd7\xac\x13\xda-\xd0\x98\x8aC\x8d'j9\x07\xa6\xc1\xd7\xac\x13\xda-\xd0\x98\x8aC\x8d'j'
'''

#creating a function to handle the diffenernt modes of DES

def DES(msg,mode,e_or_d):
        if mode == 'ECB':
                #msg = msg.encode('utf8')
                #msg=msg.decode('unicode_escape')
                #Setting the DES algorithm
                k = des("12345678", mode)
                #Have to use getKey because the key was converted to binary in the algorithm
                print ("Key      : %s" % k.getKey())
                print ("Message     : %s" % msg)
                #Encrypting the message
                if e_or_d == 'encrypt':
                        e = k.encrypt(msg).encode('hex')
                        #e = e.decode('utf-8')
                        #e=e.decode('unicode_escape')
                        
                        print ("Encrypted: %r" % e)
                        #d = k.decrypt(k.encrypt(msg))
                        #print ("Encrypted: %r" % d)
                        return e
                        
                        
                if e_or_d == 'decrypt':
                        #Decrypting the encrypted ciphertext
                        msg = msg
                        d = k.decrypt(k.encrypt(msg))
                        
                        print ("Decrypted: %r" % d.encode('hex'))
                        #print ("Decrypted: %r" % base64.b16encode(d))
        if mode == 'CBC':
                k=des("12345678", mode, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
                print ("Key      : %s" % k.getKey())
                print ("Message     : %s" % msg)
                if e_or_d == 'encrypt':
                        e = k.encrypt(msg)
                        #e = e.decode('utf-8')
                        #e=e.decode('unicode_escape')
                        print ("Encrypted: %r" % e.encode('hex'))
                if e_or_d == 'decrypt':
                        #Decrypting the encrypted ciphertext
                        d = k.decrypt(msg)
                        print ("Decrypted: %r" % d)

plaintext = "AAAABBBBAAAABBBB"
#e = DES(msg,'ECB','encrypt')
'''print()
msg = '19FF4637BB2FE77C19FF4637BB2FE77C'
DES(msg,'ECB','decrypt')'''

print("DES: ECB Encrypting & Decryption")

k = des("12345678", 'ECB')
print ("Key      : %s" % k.getKey())
print ("Message     : %s" % plaintext)
encrypted = k.encrypt(plaintext)
print ("Encrypted: %r" % encrypted.encode('hex'))
decrypted = k.decrypt(encrypted)
print ("Decrypted: %r" % decrypted)
print
print("DES: CBC Encrypting & Decryption")


ciphertext = "AAAABBBBAAAABBBB"
#Note this only works when the ciphertext and plaintext are reversed
#In the lab the lecturer had this as the plaintext and aac823f6bbe58f9eaf1fe0eb9ca7eb08
#As the ciphertext


j = des("12345678", CBC,"00000000")
print ("Key      : %s" % j.getKey())
print ("Message     : %s" % ciphertext)
encrypted = j.encrypt(ciphertext)
print ("Encrypted: %r" % encrypted.encode('hex'))
decrypted = j.decrypt(encrypted)
print ("Decrypted: %r" % decrypted)
print



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
plaintext = "AAAABBBBCCCC"
plaintext = addPadding(plaintext)
k = des("12345678", 'ECB')
print ("Key      : %s" % k.getKey())
print ("Message     : %s" % plaintext)
encrypted = k.encrypt(plaintext)
print ("Encrypted: %r" % encrypted.encode('hex'))
decrypted = k.decrypt(encrypted)
decrypted = removePadding(decrypted)
print ("Decrypted: %r" % decrypted)
print






'''
msg = 'AAAABBBBAAAABBBB'
 k=des("12345678", CBC, "00000000")
e = k.encrypt(msg)

#DES(msg,'CBC','decrypt')
print
msg = 'AAC823F6BBE58F9EAF1FE0EB9CA7EB08'
#DES(msg,'CBC','encrypt')"""
'''
