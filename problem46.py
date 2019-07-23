#All odd integers which are not prime are odd composite numbers.
import math
lis=[]
def seive(n):
            prime=[True for x in range(n+1)]
            p=2
            while(p*p<=n):
                        if(prime[p]):
                                    for i in range(p*p,n+1,p):
                                                prime[i]=False
                        p+=1
            for i in range(2,n):
                        if(prime[i]):
                                    lis.append(i)
seive(10**6)
for i in range(4,len(lis)):
            a=2*i+1
            if( a not in lis):
                        for j in range(1,a):
                                    k=j
                                    if(a-2*(j**2) in lis):
                                                break
                        if(k==a-1):
                                    print(a)
                                    break
