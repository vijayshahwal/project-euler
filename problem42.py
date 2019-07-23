l=[str(x)[1:-1] for x in input().split(",")]
result =0
for i in l:
            ref=0
            for j in i:
                        ref+=ord(j)-64
            s=ref*2
            temp = int(s**0.5)
            if(temp*(temp+1)==s):
                        result+=1
print(result)

