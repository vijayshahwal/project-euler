import math
def fun(a,b):
    n=a
    power=b
    return power*math.log(a,10)
result=0.00
line=0
for i in range(1,1001):
    a,b=[int(x) for x in input().split(",")]
    p=fun(a,b)
    if(p>result):
        result=p
        line=i
print(line)
