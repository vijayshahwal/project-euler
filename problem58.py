############# METHOD THAT NEED OPTIMIZATION ###########
"""def printSpiral(n) : 
    arr=[[0 for i in range(n)] for j in range(n)] 
    for i in range(0, n) : 
        for j in range(0, n) : 
            x = min(min(i, j), min(n - 1 - i, n - 1 - j)) 
              
            # For upper right half 
            if (i <= j) : 
                arr[i][j]=(n - 2 * x) * (n - 2 * x)-(i - x)- (j - x) 
  
            # For lower left half 
            else : 
                arr[i][j]=((n - 2 * x - 2)*(n - 2 * x - 2) +(i - x) + (j - x)) 
    return arr
          
# Driver code
n=26241
while(True):
    arr=printSpiral(n)
    count=0
    for i in range(0,n):
        if(is_prime(arr[i][i])):
            count+=1
    for i in range(0,n):
        if(i!=n-i and is_prime(arr[i][n-i-1])):
            count+=1
    print(count/(2*n-1)*100,n)
    if(count/(2*n-1)*100<10):
        print(n)
        break
    n+=1
"""
############### GENERATE ONLY DIAGONAL NUMBER or CORNER OF EVERY SQUARE #############
### (3,5,7,9)(13,17,19,21)....
import math
import random
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

side=1
count=0
n=1 # n represent layer and corresponding side length is 2*n+1
while(n<100000):
    if(is_prime(4*n*n-2*n+1)):
        count+=1
    if(is_prime(4*n*n+1)):
        count+=1
    if(is_prime(4*n*n+2*n+1)):
        count+=1
    if(is_prime(4*n*n+4*n+1)):
        count+=1
    n+=1
    if(10*count<4*n+1):
        print(2*n+1)
        break

