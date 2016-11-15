#Author: Fionn Mcguire
#Student Number: C13316356
#Assignment: Advanced Security Lab 3 (DES)



import AES
obj = AES.new('This is a key456', AES.MODE_ECB)
message = "The answer is no"
ciphertext = obj.encrypt(message)
obj2 = AES.new('This is a key456', AES.MODE_ECB)
obj2.decrypt(ciphertext)
