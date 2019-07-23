def bouncy(n):
     lis=[]
     while(n):
          lis.append(n%10)
          n//=10
     lis=list(reversed(lis))
     slis=list(sorted(lis))
     rlis=list(sorted(lis,reverse=True))
     if(lis==slis or lis==rlis):
          return False
     return True
n=10000000
num=0
den=100
for i in range(101,n):
     #print(i,bouncy(i))
     if(bouncy(i)):
          num+=1
     den+=1
     if(100*num==99*den):
          print(i)
          break
