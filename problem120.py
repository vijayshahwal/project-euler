su=0
for a in range(3,1001):
     m=0
     for n in range(1,a):
          m=max((2*a*n)%(a*a),m)
     su+=m
print(su)         
     
