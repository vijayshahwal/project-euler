import math as m
count=0
p=0
l=[]
for i in range(1,101):
            for j in range(1,101):
                        if(i>j):
                                    p=m.factorial(i)//(m.factorial(i-j)*m.factorial(j))
                                    if(p>1000000):
                                                #l.append(p)
                                                count+=1

print(count)
#print(l)
