#problem solved without programming by rahul

import math as m
lis=[]
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
			lis.append(p) 

n=510510
SieveOfEratosthenes(n)
result=0
ans=0
for i in range(10,n+1):
            phi = i
            if(i in lis):
                        phi = i-1
            else:
                        for j in range(2,int(m.sqrt(i))+1):
                                    if(i%j==0):
                                                if(j in lis):
                                                            phi *=(1-(1/j))
                                                if(i//j in lis and j != i//j):
                                                            phi *= (1-(1/(i//j)))
        
            temp =i/phi
            if(temp>result):
                        result = temp
                        ans=i
            print(result)
                        

print("final result")                                    
print(result)
print(ans)
