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
x1=[]
for i in lis:            
            num=[int(math.sqrt(i)),int(math.sqrt(i))*lis[i][0]+1]
            den=[1,lis[i][0]]
            for j in range(2,len(lis[i])):
                        num.append(num[j-1]*lis[i][j]+num[j-2])
                        den.append(den[j-1]*lis[i][j]+den[j-2])
            print(i,num)
            print(den)
            for j in range(len(num)):
                        if(num[j]**2-i*(den[j]**2)==1):
                                    x1.append([num[j],i])
                                    break
x1=sorted(x1,key=lambda element:element[1])
            
            
