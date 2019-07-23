import math
def primefactor(n):
            fact=set()
            while(n%2==0):
                        fact.add(2)
                        n=n//2
            for i in range(3,int(math.sqrt(n))+1):
                        while(n%i==0):
                                    fact.add(i)
                                    n=n//i
            if(n>2):
                        fact.add(n)
            return fact
n=1000000
for i in range(2,n):
            a=primefactor(i)
            b=primefactor(i+1)
            c=primefactor(i+2)
            d=primefactor(i+3)
            if(len(a)==len(b) and len(b)==len(c) and len(c)==len(d) and a!=b and b!=c and c!=d and len(a)==4):
                        print(i,i+1,i+2,i+3)
                        print(a,b,c,d)
                        break


