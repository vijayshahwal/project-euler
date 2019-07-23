lis=[]
for i in range(1,100):
            lis.append(1)
            lis.append(2*i)
            lis.append(1)
#print(lis)
arr=[False for x in range(101)]
def numerator(n):
            num0=2
            num1=3
            if(n==1):
                        return num1
            if(n==0):
                        return num0
            else:
                        if(arr[n-1]==False):
                                    arr[n-1]=numerator(n-1)
                        if(arr[n-2]==False):
                                    arr[n-2]=numerator(n-2)
                        arr[n]=arr[n-1]*lis[n-1]+arr[n-2]
                        return arr[n]
                        
n=100
numerator(n)
#while(False in arr):
#            arr.remove(False)
p=str(arr[99])
q=[]
for i in range(len(p)):
            q.append(int(p[i]))
print(sum(q))
