lis=[]
def Sieve(n):
   prime = [True for i in range(n+1)] 
   p = 2
   while (p * p <= n):
      if (prime[p] == True):
         for i in range(p * p, n+1, p):
            prime[i] = False
      p += 1
    
   for p in range(2, n):
      if prime[p]:
         lis.append(p)

Sieve(10**6)
coun=1
for i in lis:
   if(((i-1)**coun+(i+1)**coun)%(i**2)>10**10):
      print(i,coun)
      break
   coun+=1


