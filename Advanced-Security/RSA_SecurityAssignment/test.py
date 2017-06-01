N = 3293
e = 35
m = 153
d = 2987
p = 37
q = 89

answer = m**e%N
#print(answer)

x =answer**d%p
y = answer**d%q

remainder1 = answer%p
remainder2 = answer%q


power1 = d%(p-1)
power2 = d%(q-1)


answer1 = remainder1**power1%p
answer2 = remainder2**power2%q

X = 0
Y = 0
print(answer1,answer2)


checker = 0
X = q%p
Y = p%q
        
remainder = 1+p
while checker == 0:
    if  remainder%X == 0:
        X = remainder/X
        checker = 1
    remainder+=p

            
checker = 0
remainder = 1+q
while checker == 0:
    if  remainder%Y == 0:
        Y = remainder/Y
        checker = 1
    remainder+=q   

print(X,Y)



x = ((q*X*answer1)+(p*Y*answer2))%N

print(x)
