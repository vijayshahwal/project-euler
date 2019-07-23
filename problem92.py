def fun(n):
            p=n
            if(n==1 or n==89):
                        return n
            sm=0
            while(p!=0):
                        sm+=(p%10)**2
                        p=p//10
            return fun(sm)
count=0
for i in range(1,10**7):
            if(fun(i)==89):
                        count+=1
print(count)

