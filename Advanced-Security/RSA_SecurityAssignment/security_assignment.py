

#Fionn Mcguire
#C13316356
#DT211/3
#Security assignment (RSA encryption)

import random
import math
"""340282366920938463463374607431768211456"""
def getting_public_keys() :
    prime1 = random.randint(2, 340282366920938463463374607431768211456)
    prime2 = random.randint(2, 340282366920938463463374607431768211456)

    validation2 = 0
    while validation2 != 50:
        dividend = random.randint(2, prime1)
        print("Dividend 1 is: {0}".format(dividend))
        
        equation =  dividend**(prime1-1) % prime1
        
        print("Equation 1 is: {0}".format(equation))
        if equation == 1:
            
            validation2 += 1
        else:
            
            validation2 = 0
            prime1 = random.randint(2, 340282366920938463463374607431768211456)
    if validation2 == 50:
        print("{0} Is Prime".format(prime1))
    """
    validation2 = 0
    while validation2 != 50:
        dividend = random.randint(2, prime2)
        print("Dividend 2 is: {0}".format(dividend))
        if dividend**(prime2-1) % prime2 == 1:
            print("Is Prime")
            validation2 += 1
        else:
            print("Nevermind")
            validation2 = 0
            prime2 = random.randint(2, 340282366920938463463374607431768211456)"""

    print("Number 1: {0}".format(prime1))


print(getting_public_keys())


