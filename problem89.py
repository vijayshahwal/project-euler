d1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
d2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
d={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50
   ,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
n=1000
res=0
for j in range(1,n+1):
    x=input()
    ############# convert roman to integer #########
    num=0
    i=0
    while(i<len(x)):
        if(x[i] in d1.keys()):
            if(i+1<len(x) and x[i]+x[i+1] in d2.keys()):
                num+=d2[x[i]+x[i+1]]
                i+=2
            else:
                num+=d1[x[i]]
                i+=1
                
    ans=""
    for i in d:
        while(num>=d[i]):
            ans+=i
            num-=d[i]
    res+=abs(len(x)-len(ans))
    #print(num,x)
print(res)        
        
