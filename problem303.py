########### PROBLEM 303 #################
### This question contain patter for 9,99,999,9999
### 9------ 12222
### 99----- 1122222222
### 999---- 111222222222222
### 9999--- 11112222222222222222
## rest is easy
def base(n):
     if(n<3):
          return n
     num=""
     while(n):
          num+=str(n%3)
          n//=3
     return ''.join(reversed(num)) 
n=50000000
lis=[]
for i in range(1,n):
     lis.append(int(base(i)))
su=0
count=0
for i in range(1,10001):
     for j in lis:
          if(j%i==0 and i!=9999):
               su+=(j//i)
               #print(i,j)
               count+=1
               break
print(su,count)
