import time
import math
t1=time.time()
lis=[]
n=10**7
pr=n//2
prime=[True]*(pr+1)
p=2
while(p*p<=n):
    if(prime[p]):
        for i in range(p*p,pr+1,p):
            prime[i]=False
        
    p+=1
for i in range(2,len(prime)):
    if(prime[i]):
        lis.append(i)
def fun(i,j,n):
    if(i*j>n):
        return 0
    k=n
    count_i=int(math.log(n,i))
    count_j=int(math.log(n,j))
    z=0
    for a in range(count_j,0,-1):
        for b in range(count_i,0,-1):
            x=(j**a)*(i**b)
            if(x<=n):
                z=max(x,z)
    return z
ans=0
l=int(math.sqrt(len(lis)))+1
for i in range(0,l):
    for j in range(i+1,len(lis)):
        a=lis[i]
        b=lis[j]
        z=fun(a,b,n)
        if(z==0):
            break
        ans+=z
        #print(lis[i],lis[j],z)
t2=time.time()
print(ans)
print(t2-t1)   
