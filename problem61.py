from itertools import permutations
import math
def t3(n):
    x=(-1+math.sqrt(1+8*n))/2
    if(x==int(x)):
        return True
    return False
def t4(n):
    x=math.sqrt(n)
    if(x==int(x)):
        return True
    return False
def t5(n):
    x=1+math.sqrt(24*n+1)
    x=x/2
    if(x==int(x)):
        return True
    return False
def t6(n):
    x=1+math.sqrt(8*n+1)
    x=x/4
    if(x==int(x)):
        return True
    return False
def t7(n):
    x=3+math.sqrt(40*n+9)
    x=x/10
    if(x==int(x)):
        return True
    return False
def t8(n):
    x=1+math.sqrt(3*n+1)
    x=x/3
    if(x==int(x)):
        return True
    return False
def equal(x1,x2,x3,x4,x5,x6):
    lis=[x1,x2,x3,x4,x5,x6]
    if(len(set(lis))==len(lis)):
        return True
    return False
order=permutations([t3,t4,t5,t6,t7,t8])
for j in order:
    for i in range(1000,10000):
        x1=i
        if(j[0](x1)):
            x1_f=x1//100
            x1_l=x1%100
            for k in range(10,100):
                x2=int(str(x1_l)+str(k))
                if(j[1](x2)):
                    x2_l=x2%100
                    for l in range(10,100):
                        x3=int(str(x2_l)+str(l))
                        if(j[2](x3)):
                            x3_l=x3%100
                            for m in range(10,100):
                                x4=int(str(x3_l)+str(m))
                                if(j[3](x4)):
                                    x4_l=x4%100
                                    for n in range(10,100):
                                        x5=int(str(x4_l)+str(n))
                                        if(j[4](x5)):
                                            x5_l=x5%100
                                            for o in range(10,100):
                                                x6=int(str(x5_l)+str(o))
                                                if(j[5](x6)):
                                                    x6_l=x6%100
                                                    if(x6_l==x1_f and equal(x1,x2,x3,x4,x5,x6)):
                                                        print(x1,x2,x3,x4,x5,x6)
                                                        exit(0)
                                                        
                


