import math
def lcm(a,b):
    lc_m=(a*b)//math.gcd(a,b)
    return lc_m
count=0
def p(i,b):
    x=1
    for j in range(1,i+1):
        x=lcm(x,j)

    y=1
    for j in range(1,i+2):
        y=lcm(y,j)
    return b//x-b//y
for i in range(2,32):
    count+=p(i,pow(4,i))
    
print(count)
