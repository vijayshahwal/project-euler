lis =[]
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

#to check prime or not
def check(n):
            if (n <= 1):
                        return False
  
    # Check from 2 to n-1 
            for i in range(2, n): 
                        if (n % i == 0): 
                                    return False
  
            return True
# driver program 
n = 10000000
SieveOfEratosthenes(n)
res=0
lis1=[]
for i in range(len(lis)):
            a=lis[i]
            b=lis[i]
            count =0
            print(a)
            boolean1 = True
            boolean2 = True
            while(a!=0):
                        count+=1
                        if(check(a)==False):
                                    boolean1=False
                        a = a//10
            while(count>0):
                        if(check(b)==False):
                                    boolean2 = False
                        count-=1
                        b =b%(10**count)
            if(boolean1 and boolean2):
                        res += lis[i]
                        lis1.append(lis[i])
            if(len(lis1)==15):
                        print("found")
                        break
            
print(res)
print(lis1)
