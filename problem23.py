import math
def Sumdivisor(num):
            i=2
            result=0
            while i<= (math.sqrt(num)):
                        if (num % i == 0) : 
                                    if (i == (num / i)) : 
                                                result = result + i 
                                    else :
                                                result = result +  (i + num/i) 
                        i = i + 1
            return (result+1)
abundantnumber=[]
tempsumoftwo_abundant=[]
sumoftwo_abundant=[]
n=28
for i in range(1,n+1):
            if(Sumdivisor(i)>i):
                        abundantnumber.append(i)
lis=[]
for i in range(1,n+1):
            lis.append(i)
for i in range(len(abundantnumber)):
            for j in range(len(abundantnumber)):
                        if(abundantnumber[i]+abundantnumber[j]<n+1):
                                    tempsumoftwo_abundant.append(abundantnumber[i]+abundantnumber[j])

sumoftwo_abundant=list(set(tempsumoftwo_abundant))                                          
print(sum(lis)-sum(sumoftwo_abundant))

