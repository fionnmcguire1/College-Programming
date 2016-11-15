#Advanced Security Lab 5
#Author: Fionn Mcguire
#Student Number: C13316356
#Date: 12/11/2016

#Note the 0b at the start of the string is used to signify that it is binary,
#this is not part of the returned answer.

import scipy.special as spc
import scipy.fftpack as sff
import scipy.stats as sst
import numpy
import math
import copy
import os

#Note: monobit function was taken from the lecturers suggested site
#https://github.com/StuartGordonReid/r4nd0m
def monobit(bin_data):

    count = 0
    # If the char is 0 minus 1, else add 1
    for char in bin_data:
        if char == '0':
            count -= 1
        else:
            count += 1
    # Calculate the p value
    sobs = count / math.sqrt(len(bin_data))
    p_val = spc.erfc(math.fabs(sobs) / math.sqrt(2))
    return p_val

m = 104723*104729
xi = 9

def rng():
    global xi
    xi = (xi*xi)%m
    return bin(xi)
for i in range(20):
    bitstr = rng()
    print(bitstr)

#rng_tester = RandomnessTester(None)
p_value = monobit(bitstr)
print(p_value)

#First p_value returned 0.869417060741 when xi = 9 and m = 47713*811102
#Second p_value returned was 0.398024719507 when xi = 9 and m = 104723*104729
'''
This means that in the first instance, 87% of the changes were similar changes and therfore small,
27% of changes were quite large. This is different in the second instance where almost 40% were sililar
changes and 60% were large changes. This means this random number generator is more useful as
the larger the numbers are the more of the number specturm it will generate, i.e the numbers will not gather
and keep returning similar numbers making it a less predictable number generator. Note that this is only
relatively unpredictable if the primes provided are large.
'''
