#Lab9 Key distribution & User Authenticatio
#Author: Fionn Mcguire
#Student Number: C13316356
#Date: 15/11/2016


#Q1 Self signed certificate

from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
import binascii


'''
key = RSA.generate(2048)

binPrivKey = key.exportKey('DER')
binPubKey =  key.publickey().exportKey('DER')

def bin2hex(binStr):
    return binascii.hexlify(binStr)

def hex2bin(hexStr):
    return binascii.unhexlify(hexStr)

privkey = bin2hex(binPrivKey)
pubkey = bin2hex(binPubKey)


print("Private key: %s" % privkey)
print("Public Key: %s" % pubkey)


#openssl genrsa -out www.example.com.key 2048
'''
#Importing OpenSSL a library for creating CSR
from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join


CERT_FILE = "CSRRequest.crt"
KEY_FILE = "PrivateKeyPair.key"

def create_self_signed_cert(cert_dir):

    #Creating the files
    if not exists(join(cert_dir, CERT_FILE)) \
            or not exists(join(cert_dir, KEY_FILE)):
            
        # Creating a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        #Creating a self-signed cert X.509
        #This cert has all of my details and the details of my laptop hostname
        #Make the object x509 then fill out the details
        cert = crypto.X509()
        cert.get_subject().C = "Ir"
        cert.get_subject().ST = "Leinster"
        cert.get_subject().L = "Dublin"
        cert.get_subject().O = "DIT"
        cert.get_subject().OU = "Kevin Street"
        cert.get_subject().CN = gethostname()
        cert.set_serial_number(1)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        #Attaching the public key and hashing it, privte key must be kept private
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')

        open(join(cert_dir, CERT_FILE), "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(join(cert_dir, KEY_FILE), "wt").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

#Creating these files in my current directory, the function requires a directory
#Usually you would store these somewhere else, potentially in the browsers trust store
#This is located deep within your file system but would be more secure
#It would be better to store it here and pass the directory value into this script from a more secured file
#As to upgrade the security in the spirit of the module.
create_self_signed_cert('')
