import math
x=1000000
chain=0
def amicable(n):
    sumofdiv=1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            if(i==(n//i)):
                sumofdiv+=i
            else:
                sumofdiv+=(i+n//i)
    return sumofdiv
n=12496
while(True):
    if(amicable(n)>x):
        break
    
            
        
