import random
import math
import time
t1=time.time()
def is_prime(n):
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True
ans=0
p=150000000
counter=0
for n in range(10,p,10):
    if(is_prime(n**2+1)):
        x=n**2+1
        primecount=1
        li=[n**2+1,n**2+3,n**2+7,n**2+9,n**2+13,n**2+27]
        while(primecount<6):
            x+=2
            if(is_prime(x)):
                if(li[primecount]==x):
                    primecount+=1
                    continue
                else:
                    break
        if(primecount==6):
            print(n)
            ans+=n
t2=time.time()
print(ans)
print(t2-t1)
