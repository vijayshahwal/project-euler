#PROBLEM 80#
from decimal import *
import math
sum1=0
count=0
lis=[]
for i in range(1,11):
        lis.append(i*i)
for i in range(1,101):
        if(i in lis):
                count=1 ### no use of if block we need only else part
        else:
                getcontext().prec=102
                a=Decimal(i).sqrt()/10
                #print(a)
                for j in range(1,101):
                        a=a*10
                a=int(a)
                #print(a)
                for j in range(1,101):
                        sum1+=a%10
                        a=a//10
print(sum1)

