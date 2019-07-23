res =0
l =[]
s=1
for i in range(20):
            l.append([int(x) for x in input().split()])
#print(l)
for i in range(20):
            for j in range(20):
                        #top
                        if(i>=3):
                                    s =l[i][j]*l[i-1][j]*l[i-2][j]*l[i-3][j]
                                    if(res<s):
                                                res=s
                        #bottom
                        if(i<=16):
                                    s =l[i][j]*l[i+1][j]*l[i+2][j]*l[i+3][j]
                                    if(res<s):
                                                res=s
                        #left
                        if(j>=3):
                                    s =l[i][j]*l[i][j-1]*l[i][j-2]*l[i][j-3]
                                    if(res<s):
                                                res=s
                        #right
                        if(j<=16):
                                    s =l[i][j]*l[i][j+1]*l[i][j+2]*l[i][j+3]
                                    if(res<s):
                                                res=s
                        #left diagonal
                        if(i<=16 and j>=3):
                                    s =l[i][j]*l[i+1][j-1]*l[i+2][j-2]*l[i+3][j-3]
                                    if(res<s):
                                                res=s
                        #right  diagonal
                        if(i<=16 and j<=16):
                                    s =l[i][j]*l[i+1][j+1]*l[i+2][j+2]*l[i+3][j+3]
                                    if(res<s):
                                                res=s
print(res)
                                    
                                    
