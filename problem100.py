####   it is a diophantine equation
#####  x*(x-1)=n*(n-1)//2

import math
x=15
n=21
t=10**12
while(n<t):
     x1=3*x+2*n-2
     n1=4*x+3*n-3
     x=x1
     n=n1
print(x,n)
