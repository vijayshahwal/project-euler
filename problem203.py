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
def squarefree(n):
    count=0
    while(n%2==0):
        n//=2
        count+=1
        if(count>=2):
            return False
    for i in range(3,int(math.sqrt(n))+1,2):
        count=0
        while(n%i==0):
            n=n//i
            count+=1
            if(count>=2):
                return False
    return True
def nCr(n,r):
    if(n==r):
        return 1
    elif(n<r):
        return 1
    else:
        num=1
        den=1
        for i in range(1,r+1):
            num*=(n-i+1)
            den*=i
        return num//den
n=50  ##### starting fro ncr(0,0) first 51 will be on 50
lis=[]
for i in range(1,n+1):
    for j in range(i+1):
        x=nCr(i,j)
        if(x not in lis and squarefree(x)):
              lis.append(x)
print(sum(lis))
        
        
            
