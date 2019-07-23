#problem 30
res = 0
for i in range(1,(9**5)* 7):
            j =i
            s=0
            while(j!=0):
                        s+=(j%10)**5
                        j =j // 10
            if(i==s):
                        res+=i
                        print(i)
print(res-1)
