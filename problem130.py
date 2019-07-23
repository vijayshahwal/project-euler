import math
from eulerlib import is_prime
def fun(n):
     repunit=1
     len_rep=1
     while(repunit%n!=0):
          repunit=(repunit*10+1)%n
          len_rep+=1
     return len_rep
count=0
su=0
for i in range(2,20000):
     if(count<25 and not is_prime(i) and math.gcd(i,10)==1 and (i-1)%fun(i)==0):
          su+=i
          count+=1
print(count,su)
