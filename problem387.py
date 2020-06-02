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

lis=[]
def strongHarshadNumber(n):
    global count
    if(n>10**14):
        return
    else:
        for i in range(10):
            k=str(n)+str(i)
            s=sum(map(int,k))
            k=int(k)
            if(k%s==0 and k<10**14):
                lis.append(k)
                strongHarshadNumber(k)
            
        
t2=time.time()
for i in range(1,10):
    strongHarshadNumber(i)
ans=0
for i in lis:
    for j in range(1,10,2):
        x=int(str(i)+str(j))
        y=int(str(i))
        if(x<10**14 and is_prime(x) and is_prime(y//sum(map(int,str(i))))):
            ans+=int(str(i)+str(j))
print(ans)
print(t2-t1)
