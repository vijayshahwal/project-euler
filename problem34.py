import math as m
res =0
for i in range(1,m.factorial(9)*8):
            j =i
            s=0
            while(j!=0):
                        s +=m.factorial(j%10)
                        j=j//10
            if(i==s):
                        res +=i
                        print(i)
#print(res)
