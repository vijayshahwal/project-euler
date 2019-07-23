from itertools import permutations
import math as m
perm =[''.join(p) for p in permutations('1234567')]
res=0
def isPrime(n):
            if(n<=1):
                        return False
            for i in range(2,n):
                        if(n%i==0):
                                    return False
            return True
for i in range(m.factorial(7)):
            a = int(perm[i])
            if(isPrime(a)):
                        if(res<a):
                                    res =a
print(res)
