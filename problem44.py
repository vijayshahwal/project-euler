lis=[]
n=10000
for i in range(1,n):
    lis.append(i*(3*i-1)//2)
for i in range(1,len(lis)):
    for j in range(1,i):
        if(lis[i]+lis[j] in lis[i:] and lis[i]-lis[j] in lis[:i]):
            print(lis[i],lis[j])
            break
print(2)
