l=[]
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            l.append(p)
n=2000000
SieveOfEratosthenes(n)
def to(n):
            ref=0
            j=n
            seen = False
            result=j
            if(result in l):
                        return result-1
            else:
                        while(j!=1):
                                    if(j%l[ref]==0):
                                                if(not seen):
                                                            result*=(l[ref]-1)/l[ref]
                                                            seen=True
                                                j/=(l[ref])
                                    else:
                                                ref+=1
                                                seen=False
                        return result
su = 0
for i in range(2,1000001):
    su+=to(i)
print(su)
