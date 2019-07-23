############### PROBLEM 74 ##############
from math import factorial as f
def fun(n,lis=[]):
     su=0
     while(n):
          su+=f(n%10)
          n//=10
     if(su not in lis):
          lis.append(su)
          fun(su,lis)
     return lis
count=0
for i in range(1,1000000):
     l=fun(i,list())
     if(len(l)==59):
          count+=1

print(count)
