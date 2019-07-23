lisp=[]
import random
def sieve(n):
    prime=[True for x in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for i in range(2,n):
        if(prime[i]):
            lisp.append(i)
sieve(10000)
def is_prime(n,k=3):
    if n<6:
        return [False,False,True,True,False,True][n]
    elif n%2==0:
        return False
    else:
        s,d=0,n-1
        while d%2==0:
            s,d=s+1,d>>1
        for a in random.sample(range(2,n-2),k):
            x=pow(a,d,n)
            if(x!=1 and x+1!=n):
                for r in range(1,s):
                    x=pow(x,2,n)
                    if x==1:
                        return False
                    elif x==n-1:
                        a=0
                        break
                if a:
                    return False
        return True
"""def comb(a,b):
    len_a=math.floor(math.log10(a))+1
    len_b=math.floor(math.log10(b))+1
    x=int(a*(10**len_b)+b)
    y=int(b*(10**len_a)+a)
    if(is_prime(x) and is_prime(y)):
        return True
    return False
"""
def comb(a,b):
    x=str(a)+str(b)
    y=str(b)+str(a)
    if(is_prime(int(x)) and is_prime(int(y))):
        return True
    return False
def primepair():
    for a in lisp:
        for b in lisp:
            if a>b:
                continue
            if(comb(a,b)):
                for c in lisp:
                    if b>c:
                        continue
                    if(comb(a,c) and comb(b,c)):
                        for d in lisp:
                            if c>d:
                                continue
                            if comb(a,d) and comb(b,d) and comb(c,d):
                                for e in lisp:
                                    if d>e:
                                        continue
                                    if comb(a,e) and comb(b,e) and comb(c,e) and comb(d,e):
                                        return (a,b,c,d,e)
print(primepair())
