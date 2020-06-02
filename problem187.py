import time
import math
t1=time.time()
lis=[]
n=10**8
prime=[True]*(n+1)
p=2
while(p*p<=n):
    if(prime[p]):
        for i in range(p*p,n+1,p):
            prime[i]=False
        
    p+=1
for i in range(2,len(prime)):
    if(prime[i]):
        lis.append(i)
count=0
"""def bsearch(lis,start,end,x):
    low=start
    high=end
    while(low<high):
        mid=(low+high-1)//2
        if(lis[mid]>=x):
            high=mid
        else:
            low=mid+1
    return low
print(lis)       
for i in range(0,len(lis)):
    p=lis[i]
    q=math.floor(v/p)
    x=bsearch(lis,0,len(lis),q)
    print(p,q,x)
    count+=x
"""
i=0
while(i<len(lis) and lis[i]*lis[i]<n):
    j=i
    while(i<len(lis) and j<len(lis) and lis[i]*lis[j]<n):
        count+=1
        #print(lis[i],lis[j])
        j+=1
    i+=1
print(count)
t2=time.time()
print(t2-t1)
