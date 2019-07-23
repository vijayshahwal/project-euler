n=100
import math
c=1
prev=0
lis=[]
def digitsum(x):
            su=0
            while(x):
                        su+=x%10
                        x//=10
            return su
for i in range(2,n):
            val=i
            for j in range(1,50):
                        val*=i
                        if(digitsum(val)==i):
                                    lis.append(val)
                                    c+=1

lis.sort()
print(lis[29])
