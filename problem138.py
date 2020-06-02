m=1000
n=1
count=0
length=0
i=1
j=1
########### j=i is observation #######
while(True):
    h=i**2+j**2
    p=i**2-j**2
    b=2*i*j
    if(p==2*b+1 or p==2*b-1):
        length+=h
        #print(h,p,2*b)
        count+=1
        j=i
    if(b==2*p+1 or b==2*p-1):
        length+=h
        #print(h,b,2*p)
        count+=1
        j=i
    if(count==12):
        break
    i+=1
print(length)
