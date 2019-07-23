m=int(input())
lis=[]
for i in range(m):
            x1=[int(x) for x in input().split(" ")]
            for j in x1:
                        lis.append(j)
lis=lis+[0]*(m)
for i in range(m-1,0,-1):
            for j in range((i*(i-1))//2,int((i*(i+2))/2)):
                        #print(i,j)
                        lis[j]+=max(lis[j+i],lis[j+i+1])
print(lis[0])
