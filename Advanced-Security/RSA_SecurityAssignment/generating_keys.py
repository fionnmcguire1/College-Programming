from fractions import gcd

a = 316753
b = 304709



"""
Matrix[0][1] = 1
Matrix[1][1] = 2
Matrix[2][1] = 3
Matrix[3][1] = 4
Matrix[4][1] = 5
Matrix[5][1] = 6
Matrix[6][1] = 7
Matrix[7][1] = 8
Matrix[8][1] = 9
Matrix[9][1] = 10
Matrix[10][1] = 11
Matrix[11][1] = 12
Matrix[12][1] = 13
Matrix[13][1] = 14
Matrix[14][1] = 15
Matrix[15][1] = 16
Matrix[16][1] = 17
Matrix[17][1] = 18
Matrix[18][1] = 19
Matrix[19][1] = 20
Matrix[20][1] = 21
Matrix[21][1] = 22
Matrix[22][1] = 23
Matrix[23][1] = 24
Matrix[24][1] = 25
Matrix[25][1] = 26
Matrix[26][1] = 27
Matrix[27][1] = 28
Matrix[28][1] = 29
Matrix[29][1] = 30
Matrix[30][1] = 31
Matrix[31][1] = 32
Matrix[32][1] = 33
Matrix[33][1] = 34
Matrix[34][1] = 35
Matrix[35][1] = 36
Matrix[36][1] = 37
Matrix[37][1] = 38
Matrix[38][1] = 39
Matrix[39][1] = 40
Matrix[40][1] = 41
Matrix[41][1] = 42
Matrix[42][1] = 43
Matrix[43][1] = 44
Matrix[44][1] = 45
Matrix[45][1] = 46
Matrix[46][1] = 47
Matrix[47][1] = 48
Matrix[48][1] = 49
Matrix[49][1] = 50
Matrix[50][1] = 51
Matrix[51][1] = 52
Matrix[52][1] = 53
Matrix[53][1] = 54
Matrix[54][1] = 55
Matrix[55][1] = 56
Matrix[56][1] = 57
Matrix[57][1] = 58
Matrix[58][1] = 59
Matrix[59][1] = 60
Matrix[60][1] = 61
Matrix[61][1] = 62
Matrix[62][1] = 63
Matrix[63][1] = 64
Matrix[64][1] = 65
Matrix[65][1] = 66
Matrix[66][1] = 67
Matrix[67][1] = 68
Matrix[68][1] = 69
Matrix[69][1] = 70
Matrix[70][1] = 71
Matrix[71][1] = 72
Matrix[72][1] = 73
Matrix[73][1] = 74
Matrix[74][1] = 75
Matrix[75][1] = 76
Matrix[76][1] = 77
Matrix[77][1] = 78
Matrix[78][1] = 79
Matrix[79][1] = 80
Matrix[80][1] = 81
Matrix[81][1] = 82
Matrix[82][1] = 83
Matrix[83][1] = 84
Matrix[84][1] = 85
Matrix[85][1] = 86
Matrix[86][1] = 87
Matrix[87][1] = 88
Matrix[88][1] = 89
Matrix[89][1] = 90
Matrix[90][1] = 91
Matrix[91][1] = 92
Matrix[92][1] = 93
Matrix[93][1] = 94
Matrix[94][1] = 95
Matrix[95][1] = 96
Matrix[96][1] = 97
"""

text = 'DID IT WORK RSA ALGORITHM'
encrypted_text= ''
decrypted_text= ''
text_num= [0 for x in range(len(text))]
encrypted_num =[0 for x in range(len(text))]
decrypted_num =[0 for x in range(len(text))]

prime1 = 37
prime2 = 97

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
i = 1
check = 'true'
while check =='true':
    if (i*encryption_key)%fie_function ==1:
        decryption_key = i
        check = 'false'
    else:
        i+=1

print("Decryption Key: ",format(decryption_key))
