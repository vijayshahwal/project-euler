limit = 5*(10**7)
target = 1
from math import sqrt
Hits = [0]*(limit+1)

for d in range(1,int((limit-1)/4)):
    if 4*d**2 > limit:
        bound = int(sqrt(4*d**2-limit))+1
    else:        
        Hits[4*d**2] += 1
        bound = 1
    for t in range(bound,2*d):
        if t < d:
            i = 2
        else:
            i = 1
        Hits[4*d**2 - t**2] += i

print ("the answer is", Hits.count(target))
