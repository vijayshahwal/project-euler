import math
m=1500000 # value of m for which h<1500000 and read wikki
maxlen=5000000
sol=[0 for x in range(maxlen)]
def oppositeparity(i,j):
    if(i%2==0 and j%2==0):
        return False
    elif(i%2!=0 and j%2!=0):
        return False
    else:
        return True
for i in range(2,int(math.sqrt(m))):
    for j in range(1,i):
        if(math.gcd(i,j)==1 and oppositeparity(i,j)):
            h=i*i+j*j
            p=i*i-j*j
            b=2*i*j
            x=h+p+b
            k=1
            while(k*x<maxlen):
                sol[k*x]+=1
                k+=1
ans=0
for i in range(1,m+1):
    if(sol[i]==1):
        ans+=1
        
print(ans)
