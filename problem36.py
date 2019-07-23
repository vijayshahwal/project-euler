"""correct solution"""
a =1000000
lis =[]
tempstringlis = []
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
for i in range(a):
            j=i
            k=i
            binary1 ="{0:b}".format(k)
            binary2 =reverse(binary1)
            temp1 =str(j)
            temp2 =reverse(temp1)
            if(temp1==temp2 and binary1==binary2):
                        tempstringlis.append("{0:b}".format(i))
                        lis.append(i)
print(sum(lis))
print(len(lis))
            
                        
