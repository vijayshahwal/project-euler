################## need of dynamic programming ##########
"""res=[i for i in range(1,11)]
N=10**3
vis=[[0 for i in range(N)] for j in range(N)]
dp=[[0 for i in range(N)] for j in range(N)]
ans=0
def ways(pos,S,n):
    global ans
    if(pos==n): return int(S==0)
    dp[pos][S]=ans;
    if(vis[pos][S]):
        return ans
    vis[pos][S]=1
    ans=0
    times=0
    while(times*res[pos]<=S):
        ans+=ways(pos+1,S-times*res[pos],n)
        times+=1
    return ans
i=1
print(ways(0,10,len(res)))
while(True):
    res.append(i)
    if(ways(0,i,len(res))%10**6==0):
        print(i)
        break
    i+=1
"""
################### Euler theorem for integer partition ###########
pentagonal=[]
def fun(n):
    x=1
    while((x*(3*x-1))//2<n):
        if((x*(3*x-1))//2<n):
            pentagonal.append((x*(3*x-1))//2)
        x*=-1
        if((x*(3*x-1))//2<n):
            pentagonal.append((x*(3*x-1))//2)
        x*=-1
        x+=1

n=1000000
l=3
fun(n)
lis=[1,1,2]
while(lis[-1]%n!=0):
    i=0
    sign=1
    ans=0
    while(l-pentagonal[i]>=0):
        if(i>0 and i%2==0):
            sign*=-1
        ans+=lis[l-pentagonal[i]]*sign
        i+=1
    lis.append(ans)
    l+=1
print(len(lis)-1)
        
