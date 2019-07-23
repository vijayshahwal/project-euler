num=1
den=12345
perfect=1
total=1
def fun(n):
     if(n%2!=0):
          return False
     while(n!=1):
          if(n%2==0):
               n=n//2
          else:
               return False
     return True
for i in range(3,1000000):
     if(fun(i)):
          perfect+=1
     total+=1
     if((perfect*den)<(num*total)):
          print(i**2-i)
          break
