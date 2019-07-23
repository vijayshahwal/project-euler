import time
t=time.time()
n=10
prime=[True]*(n+1)
co=[]
for i in range(2,n+1):
     if(prime[i]==1):
          for j in range(i*i,n+1,i):
               prime[j]=False
     if(prime[i]):
          co.append(i)
def search(x=1,index=0):
     res=1
     for i in range(index,len(co)):
          product=co[i]*x
          if(product>1000000000):
               break
          res+=search(product,i)
     return res
print(search())   
t2=time.time()
print(t2-t)
