n=10000
mx=345
lis=[]
for i in range(345,n):
     lis.append(sorted(str(i**3)))
for i in lis:
     if(lis.count(i)==5):
          print(mx**3)
          break
     mx+=1

