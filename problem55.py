def palindrome(n):
    s=str(n)
    rev=''.join(reversed(s))
    if(s==rev):
        return True
    return False
def Lycher(n):
    t=n
    for i in range(50):
        x=str(t)
        y=''.join(reversed(str(t)))
        t=int(x)+int(y)
        if(palindrome(t)):
            return False
    return True
count=0
for i in range(10000):
    if Lycher(i):
        count+=1
print(count)
