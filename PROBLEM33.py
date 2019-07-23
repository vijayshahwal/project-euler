lis = []
for i in range(11,100):
            a = i//10
            b=i%10
            for j in range(i+1,100):
                        c=j//10
                        d=j%10
                        if(i%10 !=0 and j%10 !=0 and i/j==a/d and i/j<1 and i!=j and b==c):
                                    lis.append([i,j])
            

print(lis)
