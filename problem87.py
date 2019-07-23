lis=[]
def sieve(n):
            prime =[True for x in range(n+1)]
            p=2
            while(p*p<=n):
                        if(prime[p]):
                                    for i in range(p*p,n+1,p):
                                                prime[i]=False
                        p+=1
            for i in range(2,n):
                        if(prime[i]):
                                    lis.append(i)

sieve(7072)
s=set()
count=0
n=50000000
for i in range(len(lis)):
            x=lis[i]**2
            for j in range(len(lis)):
                        y=lis[j]**3
                        for k in range(len(lis)):
                                    z=lis[k]**4
                                    if(x+y+z<n):
                                                s.add(x+y+z)
                                                count+=1
                                    else:
                                                break
                                                

print(count,len(s))
############ note: count may count duplicate values but set will give exact values
