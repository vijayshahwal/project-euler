l = []
n=4
for i in range(n):
            l.append([int(x) for x in input().split(" ")])
print(l)

old_path=0
new_path=0
path=0
for i in range(n-1,-1,-1):
            new_path=0
            for j in range(0,i):
                        for k in range(0,2):
                                    if(k==0):
                                                new_path = l[i][j]+l[i-1][j]
                                                if(new_path>old_path):
                                                            old_path=new_path                                    
                                    else:
                                                new_path = l[i][j+1]+l[i-1][j]
                                                if(new_path>old_path):
                                                            old_path=new_path                                    
                                    if(old_path>path):
                                                path+=old_path
                                                print(path,old_path)

print(path)
