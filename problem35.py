lis=[]
def sieve(n):
    prime=[True for x in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i] = False
        p+=1
    for i in range(2,n):
        if(prime[i]):
            lis.append(i)
sieve(1000000)
n=1000000
total=0
t1=time.time()
for i in range(len(lis)):
    if(len(str(lis[i]))>1):
        s= str(lis[i])
        for j in range(1,len(s)):
            if(int(s[j:]+s[:j]) not in lis):
                break
        else:
            total+=1
    else:
        total+=1
t2=time.time()
print(total)
print("Time taken to compute is:",t2-t1,"second")
