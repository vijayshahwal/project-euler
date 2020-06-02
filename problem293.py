import random
import math
import time
t1=time.time()
def is_prime(n):
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True
prime=[2,3,5,7,11,13,17,19,23]
def fun(n):
    mylis=[]
    num=[1]
    lis=[6]
    c2=c3=0
    next=1
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3])
        if(next not in num):
            num.append(next)
            lis.append(next*6)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
    mylis+=lis
    lis=[2*3*5]
    num=[1]
    c2=c3=c5=0
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5])
        if(next not in num ):
            lis.append(next*30)
            num.append(next)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
        if next == 5*num[c5]: c5 += 1
    mylis+=lis
    num=[1]
    lis=[2*3*5*7]
    c2=c3=c5=c7=0
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5],7*num[c7])
        if(next not in num):
            lis.append(next*2*3*5*7)
            num.append(next)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
        if next == 5*num[c5]: c5 += 1
        if next == 7*num[c7]: c7 += 1
    mylis+=lis
    lis=[2*3*5*7*11]
    num=[1]
    c2=c3=c5=c7=c11=0
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5],7*num[c7]
                   ,11*num[c11])
        if(next not in num):
            lis.append(next*2*3*5*7*11)
            num.append(next)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
        if next == 5*num[c5]: c5 += 1
        if next == 7*num[c7]: c7 += 1
        if next == 11*num[c11]: c11 += 1
    mylis+=lis
    lis=[2*3*5*7*11*13]
    num=[1]
    c2=c3=c5=c7=c11=c13=0
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5],7*num[c7]
                   ,11*num[c11],13*num[c13])
        if(next not in num):
            lis.append(next*2*3*5*7*11*13)
            num.append(next)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
        if next == 5*num[c5]: c5 += 1
        if next == 7*num[c7]: c7 += 1
        if next == 11*num[c11]: c11 += 1
        if next == 13*num[c13]: c13 += 1
    mylis+=lis
    lis=[2*3*5*7*11*13*17]
    c2=c3=c5=c7=c11=c13=c17=0
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5],7*num[c7]
                   ,11*num[c11],13*num[c13])
        if(next not in num):
            lis.append(next*2*3*5*7*11*13*17)
            num.append(next)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
        if next == 5*num[c5]: c5 += 1
        if next == 7*num[c7]: c7 += 1
        if next == 11*num[c11]: c11 += 1
        if next == 13*num[c13]: c13 += 1
        if next == 17*num[c17]: c17 += 1
    mylis+=lis
    num=[1]
    lis=[2*3*5*7*11*13*17*19]
    c2=c3=c5=c7=c11=c13=c17=c19=0
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5],7*num[c7]
                   ,11*num[c11],13*num[c13])
        if(next not in num):
            lis.append(next*2*3*5*7*11*13*17*19)
            num.append(next)
        if next == 2*num[c2]: c2 += 1
        if next == 3*num[c3]: c3 += 1
        if next == 5*num[c5]: c5 += 1
        if next == 7*num[c7]: c7 += 1
        if next == 11*num[c11]: c11 += 1
        if next == 13*num[c13]: c13 += 1
        if next == 17*num[c17]: c17 += 1
        if next == 19*num[c19]: c19 += 1
    mylis+=lis
    lis=[2*3*5*7*11*13*17*19*23]
    c2=c3=c5=c7=c11=c13=c17=c19=c23=0    
    while(lis[-1]<n):
        next = min(2*num[c2], 3*num[c3], 5*num[c5],
                   7*num[c7], 11*num[c11], 13*num[c13],
                   17*num[c17], 19*num[c19], 23*num[c23])
        if(next not in num):
            lis.append(next*2*3*5*7*11*13*17*19*23)
            num.append(next)
        
        if next == 2*num[c2]:
            c2 += 1
        if next == 3*num[c3]:
            c3 += 1
        if next == 5*num[c5]:
            c5 += 1
        if next == 7*num[c7]:
            c7 += 1
        if next == 11*num[c11]:
            c11 += 1
        if next == 13*num[c13]:
            c13 += 1
        if next == 17*num[c17]:
            c17 += 1
        if next == 19*num[c19]:
            c19 += 1
        if next == 23*num[c23]:
            c23 += 1
    mylis+=lis
    mylis.sort()
    for i in range(len(mylis)):
        if(mylis[i]>n):
            break
    return mylis[:i]


def f(n,mylis):
    sol=[]
    for i in mylis:
        n=i
        j=3
        while(True):
            if(is_prime(n+j)):
                break
            j+=2
        if(j not in sol):
            sol.append(j)

    return sol
########## add powers of 2
n=10**9
a=fun(n)
k=int(math.log(n,2))+1
for i in range(1,k):
    if(2**i<n):
        a.append(2**i)

a.sort()
result=f(n,a)
t2=time.time()
print(sum(result))
print(t2-t1)

