################## no need of dynamic programming ##########
N=10**4
res=[]
def sieve(n):
    prime=[True]*(n+1)
    p=2
    lis=[]
    while(p*p<=n):
        if(prime[p]):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for i in range(2,len(prime)):
        if(prime[i]):
            lis.append(i)
    return lis,len(lis)
#visited=[[0 for i in range(N)] for j in range(N)]
def ways(pos,S,n):
    if(pos==n): return int(S==0)
    ans=0
    times=0
    while(times*res[pos]<=S):
        ans+=ways(pos+1,S-times*res[pos],n)
        times+=1
    return ans
x=10
while(True):
    res,n=sieve(x)
    if(ways(0,x,n)>5000):
        print(x)
        break
    x+=1
    

