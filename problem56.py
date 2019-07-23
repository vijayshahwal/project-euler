lis =[]
n=100
for a in range(1,n):
            for b in range(1,n):
                        p=a**b
                        res=0
                        while(p!=0):
                                    res+=p%10
                                    p=p//10
                        lis.append(res)
                                    

print(max(lis))
            
                                    
