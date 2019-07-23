lis=[]
n=int(input())
for i in range(n):
            l=[int(x) for x in input().split()]
            lis.append(l)
l=[]
for i in range(len(lis)):
            for j in range(len(lis[i])):
                        l.append(lis[i][j])
for i in range(n-1,0,-1):
            for j in range((i*(i-1))//2,(i*(i+1))//2,1):
                        l[j]+=max(l[j+i],l[j+i+1])
            
print(l[0])
