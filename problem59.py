encrypted=list(map(int,input().split(",")))
decoded=[]
a=97
z=122
############ remember most common english word contain [a,an,th,and,of,it]       #################################
count=0
for i in range(a,z+1):
        for j in range(a,z+1):
                for k in range(a,z+1):
                        decoded=[]
                        lis=[i,j,k]
                        for pos in range(len(encrypted)):
                                decoded.append(encrypted[pos]^lis[pos%3])
                        possible=""
                        for d in decoded:
                                possible+=chr(d)
                        if(('a ' in possible) and ('an ' in possible) and ('the ' in possible) and ('and ' in possible) and ('of ' in possible) and ('to ' in possible)):
                                asciisum=0
                                for d1 in decoded:
                                        asciisum+=d1
                                print(possible)
                                print(asciisum,i,j,k)
                                exit(0)
                   
