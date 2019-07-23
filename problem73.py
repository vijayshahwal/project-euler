import math
n=12000
count=0
a=3
b=2
for i in range(5,n+1):
     for j in range(i//a+1,(i-1)//b+1):
          if(math.gcd(i,j)==1):
               count+=1
print(count)
 ############# READ FARERY SEQUENCE FROM WIKI ####
