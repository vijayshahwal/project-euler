import math
import time
######### program is taking 191 ms need optimization 
t1=time.time()
nth_small=678910
k=0
power=1
while(True):
    x=power*math.log(2,10)
    fractional=x-int(x)
    verify=int(pow(10,fractional)*100)
    if(verify==123):
        k+=1
        #### randomly increased to increase efficiency
        power+=80
    if(k==nth_small):
         print(power-80)
        break
    power+=1
t2=time.time()
print(t2-t1)
