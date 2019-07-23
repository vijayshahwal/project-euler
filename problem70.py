lis=[]
import math
def sieve(n):
            prime=[True]*(n+1)
            p=2
            while(p*p<=n):
                        if(prime[p]):
                                    for i in range(p*p,n+1,p):
                                                prime[i]=False
                        p+=1
            for i in range(2,n):
                        if(prime[i]):
                                    lis.append(i)
sieve(10**5)
def totient(n):
            res=n
            i=0
            while(lis[i]*lis[i]<=n):
                        if(n%lis[i]==0):
                                    res-=int(res/lis[i])
                                    while(n%lis[i]==0):
                                                n=int(n/lis[i])
                        i+=1
            if(n>1):
                        res-=int(res/n)
            return res
m=10**7
t=0
for i in range(2,10**7):
            l1=list(str(i))
            l1.sort()
            l2=list(str(totient(i)))
            l2.sort()
            if(l1==l2):
                        k=i/totient(i)
                        if(k<m):
                                    m=k
                                    t=i
                                    print(i,totient(i),m)
                                    
print(m,t)
