import re
low=101010100
high=138902662
num="1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9"
for i in range(low,high,10):
     a=i+3
     n=a*a
     if(re.search(num,str(n))):
          print(a)
     a=i+7
     n=a*a
     if(re.search(str(num),str(n))):
          print(a)
