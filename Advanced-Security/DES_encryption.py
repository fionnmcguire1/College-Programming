#Author: Fionn Mcguire
#Student Number: C13316356
#Assignment: Advanced Security Lab 3 (DES)

"""
I was unable to install pycrypto successfully after spending an accumulative 16 hours
I was however able to install it somewhere on my mac using the terminal command:
CC=clang sudo -E pip install pycrypto
Then i entered the command python to bring me into the terminal python editor.
From there i was able to run the following tester code


from Crypto.Cipher import AES
obj = AES.new('This is a key456', AES.MODE_ECB)
message = "The answer is no"
ciphertext = obj.encrypt(message)
obj2 = AES.new('This is a key456', AES.MODE_ECB)
obj2.decrypt(ciphertext)

Output: 'The answer is no'

"""

"""
DES cipher in ECB mode
Q 1. Write a program to encrypt and
decrypt the following with the DES cipher in ECB mode:
Key: 12345678
Plaintext: AAAABBBBAAAABBBB
Ciphertext: 19FF4637BB2FE77C19FF4637BB2FE77C
"""

#importing des
from Crypto.Cipher import DES
#creating a new des class and specifying key and mode the mode (ECB is default anyway)
des = DES.new('12345678', DES.MODE_ECB)
#Specifying the plaintext
plaintext = 'AAAABBBBAAAABBBB'
#encrypting plaintext
ciphertext = des.encrypt(plaintext).encode('hex')
#The ciphertext printed is not ASCII i tried to convert it using all types of coding systems but was
#unsuccessful
ciphertext

ciphertext = '19FF4637BB2FE77C19FF4637BB2FE77C'
#decrypting the ciphertext
des.decrypt(ciphertext).encode('hex')

"""
DES cipher in CBC mode
Q 2. Write a program to encrypt and decrypt the following with
the DES cipher in CBC mode:
Key: 12345678
IV: 00000000
Ciphertext: AAAABBBBAAAABBBB
Plaintext: AAC823F6BBE58F9EAF1FE0EB9CA7EB08

"""


#Importing DES
from Crypto.Cipher import DES
#Defining Key and IV
key = b'12345678'
iv = b'00000000'
#creating des object
des = DES.new(key, DES.MODE_CBC, iv)
ciphertext = b'AAC823F6BBE58F9EAF1FE0EB9CA7EB08'
#Decrypting
plaintext = des.decrypt(plaintext).encode('hex')
plaintext
#Encrypting
ciphertext = des.encrypt(b'AAAABBBBAAAABBBB').encode('hex')
ciphertext



key = b'12345678'
iv = b'00000000'
#creating des object
des = DES.new(key, DES.MODE_CBC, iv)
ciphertext = b'AAC823F6BBE58F9EAF1FE0EB9CA7EB08'
#Decrypting
plaintext = des.decrypt(plaintext).encode('hex')
plaintext
#Encrypting
ciphertext = des.encrypt(b'AAAABBBBAAAABBBB').encode('hex')
ciphertext

#checking the length, if the length is not a multiple of the blocksize specified
#then this code appends the plaintext.
i=0
block_size = 8
padded = 'AAAABBBBCCCC'
if len (padded)%block_size != 0:
    to_be_appended = len (padded)%block_size
    while i < to_be_appended:
        padded +='0'
        i +=1

padded

from Crypto.Cipher import DES
#creating a new des class and specifying key and mode the mode (ECB is default anyway)
des = DES.new('12345678', DES.MODE_ECB)
#encrypting padded plaintext
ciphertext = des.encrypt(padded)














