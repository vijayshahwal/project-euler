###########problem32##########
""" IDEA OF SET WAS GIVEN BY RAHUL """
product=[]
digit={'1','2','3','4','5','6','7','8','9'}
def pandigital(str1):
            if(str1 in lis):
                        return (True)
            return (False)
for i in range(1,10):
            s1=str(i)
            for j in range(1000,10000):
                        s2=str(j)
                        s3=str(i*j)
                        result=s1+s2+s3
                        set1=set(result)
                        if(len(s1+s2+s3)==9 and len(digit.difference(set1))==0):
                                    product.append(i*j)
for i in range(10,100):
            s1=str(i)
            for j in range(100,1000):
                        s2=str(j)
                        s3=str(i*j)
                        result=s1+s2+s3
                        set1=set(result)
                        if(len(s1+s2+s3)==9 and len(digit.difference(set1))==0):
                                    product.append(i*j)
                                    

p=list(set(product))                                   
print(sum(p))
