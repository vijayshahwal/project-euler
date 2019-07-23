triangular =[]
pentagonal =[]
hexagonal =[]
n=100000
for i in range(144,n):
            hexagonal.append(i*(2*i-1))

for i in range(166,n):
            pentagonal.append(i*(3*i-1)//2)
for i in range(286,n):
            triangular.append(i*(i+1)//2)
for i in range(len(hexagonal)):
            if(hexagonal[i] in pentagonal):
                        print(hexagonal[i])
                        break
print(2)

