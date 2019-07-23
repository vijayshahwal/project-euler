import math
n=1000000
lis=[]
lis2=[]
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
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
            lis.append(p)
SieveOfEratosthenes(n)
l=[0,0]
for i in lis:
    if(i<1001):
        lis2.append(i)
    else:
        break
result=0
res=0
for a in lis2:
    for b in lis2:
        n1=0
        while(n1*n1-n1*a+b in lis):
            n1+=1
            result = n1
        if(result>res):
            res=result
            l[0],l[1]=a,b
    print(res,l[0],l[1])
        
        
"""
def isPrime(n):
            for i in range(2,n):
                        if(n%i==0):
                                    return (False)
            else:
                        return(True)
            

print(a)"""
