a=1
b=1
def pandi(n):
     s=set()
     while(n):
          s.add(n%10)
          n//=10
     if(len(s)==9 and 0 not in s):
          return True
     else:
          return False
n1=10**9
n=2
while(True):
     n+=1
     c=(a+b)%n1
     b=a
     a=c
     if(pandi(c)):
          t=n*(0.20898764024997873)-0.3494850021680094
          if(pandi(int(pow(10,t-int(t)+8)))):
               print(c)
               break
print(n)
