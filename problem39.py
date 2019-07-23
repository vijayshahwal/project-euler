lis1 = []
lis2 = []
lis3 = []
lis =[]
## take that value n for which you can cross three digit in "lis" by hit and trial
n=500
for i in range(1,n):
            for j in range(i+1,n):
                        for k in range(j+1,n):
                                    if(i+j>k and i+k>j and k+j>i and i*i+j*j==k*k):
                                                lis1.append(i)
                                                lis2.append(j)
                                                lis3.append(k)

i=0
p=len(lis1)
while(p!=0):
            lis.append(lis1[i]+lis2[i]+lis3[i])
            i+=1
            p-=1

lis.sort()
lis4 = []
lis4 = lis
countlist = list(set(lis))
countlist.sort()
lis8 =[]
for i in countlist:
            count=0
            for j in lis4:
                        if(i==j):
                                    count+=1
            lis8.append(count)
print(countlist[lis8.index(max(lis8))])

