l=[str(x) for x in input().split(",")]
l.sort()
prs=[]
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(l)):
            count =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for j in alphabet:
                        t=j
                        for k in l[i]:
                                    if(k==j):
                                                count[ord(t)-65]+=1
                                                

            for r in range(26):
                        count[r]=count[r]*(r+1)
            su =sum(count)
            prs.append(su)
#print(sum(count))                                              
#print(count[0])
for i in range(len(prs)):
            prs[i]=prs[i]*(i+1)
print(sum(prs))
