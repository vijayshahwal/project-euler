from itertools import permutations

def Substring(str1):
            num1 = int(str1[1]+str1[2]+str1[3])
            num2 = int(str1[2]+str1[3]+str1[4])
            num3 = int(str1[3]+str1[4]+str1[5])
            num4 = int(str1[4]+str1[5]+str1[6])
            num5 = int(str1[5]+str1[6]+str1[7])
            num6 = int(str1[6]+str1[7]+str1[8])
            num7 = int(str1[7]+str1[8]+str1[9])
            if(num1%2==0 and num2%3==0 and num3%5==0 and num4%7==0 and num5%11==0 and num6%13==0 and num7%17==0):
                        return (True)
            return (False)

perm = ["".join(p) for p in permutations("0123456789")]
sum1=0
for i in range(len(perm)):
            if(Substring(perm[i])):
                        sum1+=int(perm[i])

print(sum1)
