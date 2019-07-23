from itertools import permutations

perm =["".join(x) for x in permutations("123456789")]
n=6
result=9
"""for j in range(1,10):
            result=j
            for i in range(1,n):
                        result*=i
                        temp=result
                        if(str(temp) in perm):
                                    print(result)
                                    
"""
def digitcount(n):
            count=0
            while(n!=0):
                        count+=1
                        n=n//10
            return count
##########PROBLEM 38?############
prefinal=0
#############10,000########is a random guess ################################
for j in range(2,10000):
            s=""
            for i in range(1,j):
                        res=j*i
                        temp=res
                        s+=str(temp)
                        tes=int(s)
                        if(digitcount(tes)>9):
                                    break
                        else:
                                    if(s in perm):
                                                final=int(s)
                                                if(final<987654321):
                                                            print(final)

print(prefinal)
