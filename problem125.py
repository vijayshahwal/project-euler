size=100000000
sq=int(size**0.5)
l=[0]*(sq+1)
l[1]=1
squ=[x**2 for x in range(0,sq+1)]
su=0
le=0
palin=[]
for i in range(2,sq+1):
     l[i]=l[i-1]+squ[i]
     if(l[i]<size):
         s=str(l[i])
         if(s==''.join(reversed(s)) and s not in palin):
             palin.append(int(s))
             le+=1
             #print("from 1 to ",i,"palin",s)
             su+=l[i]
     ref=l[i]
     for j in range(1,i-1):
         ref-=squ[j]
         if(ref<size):
             s=str(ref)
             if(s==''.join(reversed(s))):
                le+=1
                if(ref not in palin):
                     palin.append(ref)
                #print("from",j+1,"to",i,"palin",s)
                su+=ref
                
print(le)
print(sum(palin))
