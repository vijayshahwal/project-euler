######## A = 1/2*[x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)] #######
def areaof(x1,y1,x2,y2,x3,y3):
    return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
count=0
for i in range(1000):
    vertices = [int(x) for x in input().split(",")]
    #print(vertices)
    A=areaof(vertices[0],vertices[1],vertices[2],vertices[3],vertices[4],vertices[5])
    a1=areaof(0,0,vertices[2],vertices[3],vertices[4],vertices[5])
    a2=areaof(vertices[0],vertices[1],0,0,vertices[4],vertices[5])
    a3=areaof(vertices[0],vertices[1],vertices[2],vertices[3],0,0)
    print(A,a1,a2,a3,a1+a2+a3)
    if(A==a1+a2+a3):
        count+=1
print(count)
