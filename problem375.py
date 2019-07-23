import math
import eulerlib as l
arr=[2]
def sieve(n): 
  
    # prime[i] is going to store  
    # true if if i*2 + 1 is composite. 
    prime = [0]*int(n / 2); 
  
    # 2 is the only even prime so  
    # we can ignore that. Loop  
    # starts from 3. 
    i = 3 ; 
    while(i * i < n): 
        # If i is prime, mark all its 
        # multiples as composite 
        if (prime[int(i / 2)] == 0): 
            j = i * i; 
            while(j < n):  
                prime[int(j / 2)] = 1; 
                j += i * 2; 
        i += 2; 
  
    # Printing other primes 
    i = 3; 
    while(i < n): 
        if (prime[int(i / 2)] == 0):
            if((i-1)%4!=0):
                        arr.append(i); 
        i += 2; 
sieve(300)
print(arr)
#print(len(arr))
def divisor(n):
    cond=False
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            if(l.is_prime(i+n//i)):
                cond=True
            else:
                print(n)
                cond=False
                break
    return cond

sum1=0
count=1 #count for 1 in initial
for i in range(len(arr)):
            if(divisor(arr[i]-1)):
                        count+=1
                        sum1+=arr[i]-1
print(count*2,sum1)

