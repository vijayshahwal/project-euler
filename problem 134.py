import time
t1=time.time()
lis=[]
n=10**6+10
prime=[True]*(n+1)
p=2
while(p*p<=n):
    if(prime[p]):
        for i in range(p*p,n+1,p):
            prime[i]=False
        
    p+=1
for i in range(5,len(prime)):
    if(prime[i]):
        lis.append(i)
ans=0
def fun(x,y):
    #################### very very slow ##############
    """n=str(x)
    i=1
    while(True):
        a=int(str(i)+n)
        if(a%y==0):
            return a
        i+=1
   """
    ########## optimized (solve linear congurency by inverse modulo calculation)
    y_count=len(str(x))
    div=y-x
    a=10**y_count%y
    res=pow(a,y-2,y)*div
    res=res%y
    return 10**y_count*res+x
    
for i in range(0,len(lis)-1):
    x=lis[i]
    y=lis[i+1]
    z=0
    if(x<=n-10):
        z=fun(x,y)
        ans+=z
        #print(z,x,y)
t2=time.time()
print(ans)
print(t2-t1)
