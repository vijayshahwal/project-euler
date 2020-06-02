import math
import random
import time
#################### Need optimization    ##############
t1=time.time()
n=10**8
prime=[True]*(n+1)
lis=[]
p=2
while(p*p<=n):
    if(prime[p]):
        for i in range(p*p,n+1,p):
            prime[i]=False
            
    p+=1
for i in range(2,len(prime)):
    if(prime[i]):
        lis.append(i)
"""for i in range(3,n):
    fact.append(fact[i-1]*i)
def fun(p,fact):
    su=0
    for i in range(5,0,-1):
        su+=fact[p-i]
    return su%p
ans=0

count=0
"""
res=0
for i in range(2,len(lis)):
    x=lis[i]
    ans=x-1
    ans+=x-pow(x-1,x-2,x)
    ans+=x-pow(((x-1)*(x-2))%x,x-2,x)
    ans+=x-pow(((x-1)*(x-2)*(x-3))%x,x-2,x)
    ans+=x-pow(((x-1)*(x-2)*(x-3)*(x-4))%x,x-2,x)
    #print(x,ans,x-1,pow(x-1,x-2,x),pow((x-1)*(x-2),x-2,x),pow((x-1)*(x-2)*(x-3),x-2,x),pow((x-1)*(x-2)*(x-3)*(x-4),x-2,x))
    ans=ans%x
    res+=ans
print(res)

t2=time.time()
print(t2-t1)
