#C13316356
#Fionn Mcguire
#Lab 4 AES
#12/11/2016

def addPadding(msg):
        length = 16-(len(msg)%16)
        i=0
        while(i<length):
                msg +="0"
                i+=1
        return msg

def removePadding(msg):
        str1 = "0"
        position = msg.find(str1,0)
        msg = msg[:position]
        return msg

def removePadding1(msg):
        str1 = "\00"
        position = msg.find(str1,0)
        msg = msg[:position]
        return msg

#1 Encrypt & Decrypt AES ECB

from Crypto.Cipher import AES
import base64
ciphertext = ''
message = ''
obj = AES.new('1234567812345678', AES.MODE_ECB)

message = "AAAABBBBCCCCDDDDAA"
message = addPadding(message)
#msg = addPadding(message)
print(message)
#message = base64.b16encode(message)
ciphertext = obj.encrypt(message)
ciphertext = base64.b16encode(ciphertext)
print(ciphertext)

#Ciphertext = 43D3215C92A75A1478FCF9CB950D20DBF6B6DB7F515F89B31166DBA798CFCE56

#from Crypto.Cipher import AES
#import base64
obj = AES.new('1234567812345678', AES.MODE_ECB)
message = "43D3215C92A75A1478FCF9CB950D20DBF6B6DB7F515F89B31166DBA798CFCE56"
plaintext = obj.decrypt(base64.b16decode(message))
plaintext = removePadding(plaintext)
print(plaintext)

#Plaintext = AAAABBBBCCCCDDDDAA

#Q2 Brute Force AES

'''You would only try to break AES is you had a known translation
therfore i got the md5 of the known translation AAAABBBBCCCCDDDDAA1 to
compare against the result'''
#To run this lab takes roughly 8 seconds
from Crypto.Cipher import AES
import base64
import hashlib
with open('dictionary_file_lab_4.txt', 'r+') as f:
    lines = f.readlines()
    #lines[1]
    condition = 'true'
    i = 0
    while i < len(lines):    
        obj = AES.new(str(lines[i][0:16]), AES.MODE_ECB)
        message = "43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD"
        plaintext = obj.decrypt(base64.b16decode(message))
        plaintext = removePadding(plaintext)
        md5_number = hashlib.md5(plaintext).hexdigest()
        if md5_number == "46800683e23c3c26f60061ad5a9cdad3":
            print("Success")
            print(plaintext)
            print(lines[i])
            i = 500000
        else:
            i =i+1

''' Creating the dictionary file with a list of
keys to test, this can be appended r recreated to have every 16 diget number or character combination
but for the purpose of demonstrating how it can be done i kept it 500,000 entries long containing the known
key'''

'''
text_file = open("dictionary_file_lab_4.txt", "w")
key = 1234567812000000
while key < 1234567812500000:
    text_file.write("%s\n" % key)
    key+=1

#Key = 1234567812345678

'''
