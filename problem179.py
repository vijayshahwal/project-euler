n=10**7
sumdiv=[0]*(n+1)
for i in range(1,n):
    for j in range(i,n,i):
        sumdiv[j] += 1
#print(sumdiv)
count=0
for i in range(1,n-1):
    if(sumdiv[i]==sumdiv[i+1]):
        count+=1
print(count)
