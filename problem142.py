import math
n=1000000
isSquare=[0]*(n)
for i in range(0,int(math.sqrt(n))):
    isSquare[i*i]=1

    
for a in range(3,n):
    parity=a%2
    #### to generate a,b both even or bot odd
    for b in range(parity,a,2):
        x=(a**2+b**2)//2
        y=a**2-x
        if(x<=y):
            break
        c=int(math.sqrt(x))
        while(True):
            z=c**2-x
            if(y<=z):
                break
            if(isSquare[x-z] and isSquare[y+z] and isSquare[y-z]):
                print(x,y,z)
                exit(0)
            c+=1
            
