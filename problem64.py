lis=dict()
import math
def hcf(a,b):
            if(b==0):
                        return a
            return hcf(b,a%b)

def conti(n):
            z=x=m=1
            while n>m*m:
                        m+=1
            m=y=m-1
            l=[]
            while-z<x:x=(n-y*y)//x;y+=m;l+=y//x,;y=m-y%x;z=-1
            return (l)
count=0
for i in range(2,10000):
            if(math.sqrt(i)-math.ceil(math.sqrt(i))!=0):
                        lis[i]=conti(i)
                        if(len(conti(i))%2!=0):
                                    count+=1
print(count)
