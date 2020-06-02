N=1000000007
"""
def s(n):
    if(n<10):
        return n
    if(n%9==0):
        return int("9"*(n//9))
    else:
        x=n//9
        last="9"*(x)
        first=str(n-9*x)
        return int(first+last)
def S(n):
    ans=0
    for i in range(1,n+1):
        ans+=s(i)
    return ans

fib=[0,1]
while(len(fib)<90):
    x=fib[-1]+fib[-2]
    fib.append(x)
ans=0
for j in range(1,20):
    x=S(fib[j])
    ans+=x
    print(x%N,fib[j])

"""
def S(n):
    ######## enter n>10 so that k>1
    if(n<10):
        return (n*(n+1))//2
    k=n//9
    ans=6*pow(10,k,N)-6-9*k
    ans%=N
    x=2
    for _ in range(n%9):
        ans+=x*pow(10,k,N)-1
        ans%=N
        x+=1
    return ans%N

fib=[0,1]
for i in range(2,91):
    x=fib[-1]+fib[-2]
    fib.append(x)
ans=0
for i in range(2,91):
    x=S(fib[i])%N
    ans+=x
    ans%=N
    #print(S(fib[i]),fib[i])
print(ans)

