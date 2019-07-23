lis1=[]
def printSpiral(n):
   for i in range(0, n):
      for j in range(0, n):
# Finds minimum of four inputs 
         x = min(min(i, j), min(n-1-i, n-1-j))	     
# For upper right half 
         if(i <= j):
            lis1.append((n-2*x)*(n-2*x)-(i-x)-(j-x))
# For lower left half
         else:
            lis1.append((n-2*x-2)*(n-2*x-2)+(i-x)+(j-x)) 
		
n = 1001
printSpiral(n) 
lis3=[]
for i in range(n):
   if(i==0):
      lis3.append(lis1[:n])
   else:
      lis3.append(lis1[n*i:n*i+n])
sum1=0
for i in range(n):
   for j in range(n):
      if(i==j):
         sum1+=lis3[i][j]
      if(j==n-i):
         sum1+=lis3[i][j]

print(sum1)
