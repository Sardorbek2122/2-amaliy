import math
x=int(input('x= '))
n=int(input('n= '))
S=0
for i in range(1,n+1):
    S=S+pow(x,i)/(math.factorial(i))
print(S)
