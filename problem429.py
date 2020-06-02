import time
t1=time.time()
prime=[]
product=1
######## let n!=a*b*c.....*r than 1+a**2+b**2+....+a**2*b**2*c**2..r**2=(1+a**2)
######### *(1+b**2)*(1+c**2)*(1+d**2)....*(1+r**2)
def sieve(n):
    lis=[True]*(n+1)
    p=2
    while(p*p<=n):
        if(lis[p]):
            for i in range(p*p,n+1,p):
                lis[i]=False
        p+=1
    for i in range(2,len(lis)):
        if(lis[i]):
            prime.append(i)
n=10**8
N=int(1e9)+9
sieve(n)
############### print(prime)
unitary_divisor=[]
ans=1
print(len(prime))
for i in range(len(prime)):
    x=prime[i]
    count=0
    y=n
    while(y):
        y=y//x
        count+=y
    t=pow(pow(x,count,N),2,N)
    unitary_divisor.append(t)

for i in unitary_divisor:
    ans*=(1+i)
    ans%=N
t2=time.time()
print(ans)
print(t2-t1)
