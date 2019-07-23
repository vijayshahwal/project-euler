import math
def factors(n):
    count=0
    ans=1
    while(n%2==0):
        n//=2
        count+=1
    ans*=(2*count+1)     
    for i in range(3,int(math.sqrt(n))+1,2):
        count=0
        while(n%i==0):
            n//=i
            count+=1
        ans*=(2*count+1)
    return ans
n=1000000
for i in range(2,n):
    x=factors(i)
    if((x+1)//2>1000):
        print(i,x)
        break
