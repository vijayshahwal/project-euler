import math
from eulerlib import is_prime
def fun(n):
     if(is_prime(n) or math.gcd(n,10)!=1):
          return 0
     repunit=1
     len_rep=1
     while(repunit%n!=0):
          repunit=(repunit*10+1)%n
          len_rep+=1
     return len_rep
n=1000001
l=n
####### A(n) < n therefore start looking form n 
while fun(n)<l:
     n+=2
print(n)
