from fractions import gcd
import math
from math import floor
import sys
import random
import tkinter
from tkinter import *
from tkinter import ttk

bit_number = 0
    


text = 'DID IT WORK RSA ALGORITHM'
text_num= [0 for x in range(len(text))]

Matrix = [[0 for x in range(2)] for x in range(97)]

"""Get a text file with every symbol in the alphabet
then read from that file directly into this array using a length
specified for loop"""
Matrix[0][0] = 'A'
Matrix[1][0] = 'B'
Matrix[2][0] = 'C'
Matrix[3][0] = 'D'
Matrix[4][0] = 'E'
Matrix[5][0] = 'F'
Matrix[6][0] = 'G'
Matrix[7][0] = 'H'
Matrix[8][0] = 'I'
Matrix[9][0] = 'J'
Matrix[10][0] = 'K'
Matrix[11][0] = 'L'
Matrix[12][0] = 'M'
Matrix[13][0] = 'N'
Matrix[14][0] = 'O'
Matrix[15][0] = 'P'
Matrix[16][0] = 'Q'
Matrix[17][0] = 'R'
Matrix[18][0] = 'S'
Matrix[19][0] = 'T'
Matrix[20][0] = 'U'
Matrix[21][0] = 'V'
Matrix[22][0] = 'W'
Matrix[23][0] = 'X'
Matrix[24][0] = 'Y'
Matrix[25][0] = 'Z'
Matrix[26][0] = '0'
Matrix[27][0] = '1'
Matrix[28][0] = '2'
Matrix[29][0] = '3'
Matrix[30][0] = '4'
Matrix[31][0] = '5'
Matrix[32][0] = '6'
Matrix[33][0] = '7'
Matrix[34][0] = '8'
Matrix[35][0] = '9'
Matrix[36][0] = ' '
Matrix[37][0] = '-'
Matrix[38][0] = '_'
Matrix[39][0] = '%'
Matrix[40][0] = '@'
Matrix[41][0] = '$'
Matrix[42][0] = '.'
Matrix[43][0] = '!'
Matrix[44][0] = '&'
Matrix[45][0] = '*'
Matrix[46][0] = '^'
Matrix[47][0] = '('
Matrix[48][0] = ')'
Matrix[49][0] = '+'
Matrix[50][0] = '='
Matrix[51][0] = '{'
Matrix[52][0] = '}'
Matrix[53][0] = '['
Matrix[54][0] = ']'
Matrix[55][0] = ':'
Matrix[56][0] = ';'
Matrix[57][0] = '?'
Matrix[58][0] = '<'
Matrix[59][0] = '>'
Matrix[60][0] = '/'
Matrix[61][0] = '\\'
Matrix[62][0] = '|'
Matrix[62][0] = '\''
Matrix[63][0] = '"'
Matrix[64][0] = '~'
Matrix[65][0] = '`'
Matrix[66][0] = '±'
Matrix[67][0] = '§'
Matrix[68][0] = 'a'
Matrix[69][0] = 'b'
Matrix[70][0] = 'c'
Matrix[71][0] = 'd'
Matrix[72][0] = 'e'
Matrix[73][0] = 'f'
Matrix[74][0] = 'g'
Matrix[75][0] = 'h'
Matrix[76][0] = 'i'
Matrix[77][0] = 'j'
Matrix[78][0] = 'k'
Matrix[79][0] = 'l'
Matrix[80][0] = 'm'
Matrix[81][0] = 'n'
Matrix[82][0] = 'o'
Matrix[83][0] = 'p'
Matrix[84][0] = 'q'
Matrix[85][0] = 'r'
Matrix[86][0] = 's'
Matrix[87][0] = 't'
Matrix[88][0] = 'u'
Matrix[89][0] = 'v'
Matrix[90][0] = 'w'
Matrix[91][0] = 'x'
Matrix[92][0] = 'y'
Matrix[93][0] = 'z'
Matrix[94][0] = '€'
Matrix[95][0] = '#'
Matrix[96][0] = '¢'




i = 0
for i in range(97):
    Matrix[i][1] = i

import random
import math
import sys




def rabin_miller(n):
     s = n-1
     t = 0
     while s and 1 == 0:
         s = s/2
         t +=1
     k = 0
     while k<128:
         a = random.randrange(2,n-1)
         #a^s is computationally infeasible.  we need a more intelligent approach
         #v = (a**s)%n
         #python's core math module can do modular exponentiation
         v = pow(a,s,n) #where values are (num,exp,mod)
         if v != 1:
             i=0
             while v != (n-1):
                 if i == t-1:
                     return False
                 else:
                     i = i+1
                     v = (v**2)%n
         k+=2
     return True
    


def check_prime(n):
    root_of_n = math.sqrt(n)
    """print(root_of_n)"""
    if n < 2:
        return False
    if n%2 == 0:
        return False
    i = 3
    while i < root_of_n:
        if n%i == 0:
            return False
        i+=2
    
    return True


def egcd(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    return (lastX, lastY)


"""Generating variables needed for encryption and decryption"""

def generating_keys(prime1,prime2):
    fie_function = (prime1-1)*(prime2-1)
    print("Fie Function: ",format(fie_function))

    N = prime1*prime2
    print("N: ",format(N))
    i =2
    encryption_key=0

    while i < fie_function and encryption_key ==0:
        if gcd(N,i) == 1 and gcd(fie_function,i) == 1:
                encryption_key=i
        i+=1
    print("Encryption Key: ",format(encryption_key))

    decryption_key = 0


    decryption_key,irrelivant = egcd(encryption_key, fie_function)
    decryption_key = decryption_key%fie_function
    
    

    print("Decryption Key: ",format(decryption_key))

    return [fie_function,N,decryption_key,encryption_key]


def rsa_encryption(fie_function,N,decryption_key,encryption_key):
    encrypted_text= ''
    encrypted_num =[0 for x in range(len(text))]
    i = 0
    while i < len(text):
        j = 0
        while j < len(Matrix):   
            if text[i] == Matrix[j][0]:
                encrypted_text+=Matrix[j][0]
                text_num[i]+=Matrix[j][1]
            j+=1
        i+=1
    print(encrypted_text)
    """print(text_num)"""
    print('')

    i =0
    while i < len(text):
        j = 0
        while j < len(Matrix):   
            if text[i] == Matrix[j][0]:
                encrypted_num[i] = ((Matrix[j][1]**encryption_key)%N)
            j+=1
        i+=1

    """print(encrypted_num)"""


    """So for some reason the mod didn't work and the encryption
    text couldn't be converted so this is a form of manually converting it.
    For some reason the encrypt & decrypt works but the encrypt
    text doesn't work."""
    encrypted_text = ''
    i = 0
    while i < len(text):
        j = 0
        while j < len(Matrix):
            converted = encrypted_num[i]%97
            if converted == Matrix[j][1]:
                encrypted_text+=Matrix[j][0]
            j+=1
        i+=1
    print(encrypted_text)
    print('')

    return[encrypted_text,encrypted_num]


def rsa_decryption(fie_function,N,decryption_key,encryption_key):
    decrypted_text= ''
    decrypted_num =[0 for x in range(len(text))]
    i=0
    while i < len(text):
        decrypted_num[i] = encrypted_num[i]**decryption_key%N
        i+=1

    """print(decrypted_num)"""

    i = 0
    while i < len(text):
        j = 0
        while j < len(Matrix):   
            if decrypted_num[i] == Matrix[j][1]:
                decrypted_text+=Matrix[j][0]
            j+=1
        i+=1


    print(decrypted_text)

    return[decrypted_text,decrypted_num]

def generate_primes(bit_number):
    
    
    prime1 = random.getrandbits(bit_number)
    prime2 = random.getrandbits(bit_number)
    check_prime(prime1)
    while check_prime(prime1) == False:
        prime1 = random.getrandbits(bit_number)
        
    
    check_prime(prime2)
    while check_prime(prime2) == False:
        prime2 = random.getrandbits(bit_number)
        
    fie_function = 0
    N = 0
    decryption_key = 0
    encryption_key = 0
    fie_function,N,decryption_key,encryption_key = generating_keys(prime1,prime2)
    print(prime1,prime2)
    
    return[fie_function,N,decryption_key,encryption_key]
    


"""
need to pass fie_function,N,decryption_key,encryption_key back for this shit to happen
"""
fie_function,N,decryption_key,encryption_key = generate_primes(50)
encrypted_text,encrypted_num = rsa_encryption(fie_function,N,decryption_key,encryption_key)
decrypted_text,decrypted_num = rsa_decryption(fie_function,N,decryption_key,encryption_key)
