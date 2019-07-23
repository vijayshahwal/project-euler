n=100000
lis=[1]*(n+1)
for i in range(2,n+1):
   if(lis[i]==1):
      for j in range(i,n+1,i):
         lis[j]*=i
l=[]
for i in range(1,n+1):
   l.append([i,lis[i]])
l1=sorted(l,key=lambda x:x[1])
print(l1[10000-1][0])
