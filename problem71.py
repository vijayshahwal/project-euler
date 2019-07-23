import math
import sys
limit=10**6
a=3
b=7
s=1
r=0
for q in range(limit,2,-1):
    p=math.floor((q*a-1)//b)
    if(p*s>r*q):
        s=q
        r=p
sys.stdout.write(str(str(r)+"/"+str(s))+"\n")
