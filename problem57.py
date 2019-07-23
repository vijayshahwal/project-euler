num=1
den=2
new_nu
m=num*den+1
new_den=den
n=10
count1=0
def countdigit(n):
            count=0
            while(n!=0):
                        count +=1
                        n=n//10
            return count
print(new_num,new_den)
# note in this particular problem pattern is observed
for i in range(n-1):
            tem=new_den
            new_num =new_den*1+new_num
            new_den =new_num+tem
            temp=new_num       
            new_num=new_den
            new_den=temp
            if(countdigit(new_num)>countdigit(new_den)):
                        count1 += 1
            print(new_num,new_den)
print(count1)
