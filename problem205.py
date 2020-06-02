def ncr(n,r):
    if(n<r):
        return 0
    elif(n==r):
        return 1
    else:
        x=min(r,n-r)
        num=1
        den=1
        while(x):
            num*=n
            n-=1
            den*=x
            x-=1
        return num//den
def wayscolin(n):
    ans=0
    for i in range(7):
        ans=ans+((-1)**i)*ncr(6,i)*ncr(n-(1+6*i),5)
    return ans
def waysPeter(no_of_ways_pyramid):
    for a in [1,2,3,4]:
        for b in [1,2,3,4]:
            for c in [1,2,3,4]:
                for d in [1,2,3,4]:
                    for e in [1,2,3,4]:
                        for f in [1,2,3,4]:
                            for g in [1,2,3,4]:
                                for h in [1,2,3,4]:
                                    for i in [1,2,3,4]:
                                        no_of_ways_pyramid[a+b+c+d+e+f+g+h+i]+=1
    return no_of_ways_pyramid
                    
    
    
no_of_ways_cube={1:0,2:0,3:0,4:0,5:0}
for i in range(6,37):
    no_of_ways_cube[i]=wayscolin(i)
#print("no_of_ways_cube ",no_of_ways_cube)

no_of_ways_pyramid={}
for i in range(1,37):
    no_of_ways_pyramid[i]=0
no_of_ways_pyramid=waysPeter(no_of_ways_pyramid)
#print("no_of_ways_pyramid",no_of_ways_pyramid)

count=0
total=4**9*6**6
for i in range(9,37):
    for j in range(6,i):
        count+=no_of_ways_cube[j]*no_of_ways_pyramid[i]
print(round(count/total,7))


