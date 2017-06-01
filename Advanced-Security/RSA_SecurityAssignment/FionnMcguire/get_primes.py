prime_file = open('primes.txt','w') 


test = 4
if test == 4:

    i =2
    """340282366920938463463374607431768211456"""
    while i < 1000000:
        j =2
        validation = 0
        while j< i and validation == 0:
            if i%j == 0 and i != j and i!=1:
                
                validation =1
            else:
                j += 1
                

                
        
        if validation == 0:
             print("{0} is prime".format(i))
             prime_file.write('{0},'.format(i))
        i+=1
prime_file.close()

print("Done")
    
    
