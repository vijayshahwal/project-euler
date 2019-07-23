def fun(n):
            if(n==1):
                        return 0
            if(n%2==0):
                        return fun(n/2)+1
            if(n%2!=0):
                        return fun(3*n+1)+1

max2=0
for i in range(1,1000000):
            max1=fun(i)+1
            if(max1>max2):
                    temp=i
                    max2=max1

print(max2,temp)

