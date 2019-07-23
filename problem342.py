############### NOT WORKING for 10**10 but correct solution ##########
######### 10**4---62061
######### 10**5---923941
######### 10**6---23294055
######### 10**7---563098362
######### 10**8---12763513758
######### 10**9---284309442749
######### 10**10---5943040885644
import math as m
import sys
n=10**9
totient=[0]*(n+1)
for i in range(1,n+1):
     totient[i]=i**2
co=0
for i in range(2,n):
     if(totient[i]==i**2):
          for j in range(i,n,i):
               totient[j]-=totient[j]/i
     cube=round(totient[i]**(1./3.))
     if(cube**3==totient[i]):
          print(i,totient[i])
          co+=i
print(co)          
