#Lab 6 Stream Cipher
#Author: Fionn Mcguire
#Student Number: C13316356
#Date: 14/11/2016

#This code is to be run in terminal
#Stream cipher text length must have a remainder of 0 when divided by the key length.

from Crypto.Cipher import ARC4
obj1 = ARC4.new('01234567')
obj2 = ARC4.new('01234567')
text = 'abcdefghijklmnop'
cipher_text = obj1.encrypt(text)
cipher_text.encode('hex')
plaintext = obj2.decrypt(cipher_text)
plaintext



