#Lab 8 Diffie Hellman & RSA
#Author: Fionn Mcguire
#Student Number: C13316356
#Date: 15/11/2016

#Q1 Diffie Hellman Key Agreement

prime_mod = 23
base = 5

alice_secret_integer = 6
bob_secret_integer = 15

def diffie_hellman(prime_mod,base,alice_secret_integer,bob_secret_integer):
    
    alice_enhanced_secret_integer = base**alice_secret_integer%prime_mod
    bob_enhanced_secret_integer =  base**bob_secret_integer%prime_mod

    #print(alice_enhanced_secret_integer)
    #print(bob_enhanced_secret_integer)

    alice_key = bob_enhanced_secret_integer**alice_secret_integer%prime_mod
    bob_key =  alice_enhanced_secret_integer**bob_secret_integer%prime_mod

    #print(alice_key)
    #print(bob_key)
    return alice_enhanced_secret_integer,bob_enhanced_secret_integer,alice_key,bob_key

alice_enhanced_secret_integer,bob_enhanced_secret_integer,alice_key,bob_key = diffie_hellman(prime_mod,base,alice_secret_integer,bob_secret_integer)

print("Alice Enhanced Key: %s" % alice_enhanced_secret_integer)
print("Bob Enhanced Key: %s" % bob_enhanced_secret_integer)
print("Alice Secret Key: %s" % alice_key)
print("Bob Secret Key: %s" %bob_key)

#2 RSA Encryption

from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode



key = RSA.generate(2048)

binPrivKey = key.exportKey('DER')
binPubKey =  key.publickey().exportKey('DER')

privKeyObj = RSA.importKey(binPrivKey)
pubKeyObj =  RSA.importKey(binPubKey)

msg = "hello my name is fionn"
emsg = pubKeyObj.encrypt(msg, 'x')[0]
dmsg = privKeyObj.decrypt(emsg)
print(msg)
print(emsg.encode('hex'))
print(dmsg)
assert(msg == dmsg)
