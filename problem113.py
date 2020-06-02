import time
t1=time.time()
############### BEAUTIFUL PROBLEM ########
def increasing(n_digits):
    n_digits -= 1
    lis=[1,2,3,4,5,6,7,8,9]
    while(n_digits):
        su_m = sum(lis)
        n = len(lis)
        for i in range(len(lis)-1):
            x = lis[n-i-1]
            lis[n-i-1] = su_m
            su_m = su_m - x
        #print(lis,sum(lis))
        n_digits-=1
    return sum(lis)
def decreasing(n_digits):
    n_digits-=1
    lis=[2,3,4,5,6,7,8,9,10]
    while(n_digits):
        su_m = sum(lis) + 1
        n = len(lis)
        for i in range(len(lis)):
            x = lis[n-1-i]
            lis[n-1-i] = su_m
            su_m = su_m - x
        n_digits -= 1
    return sum(lis)
def notBouncy(n_digits):
    x=n_digits
    n_digits-=1
    if(n_digits == 0):
        return 0
    ans = 0
    k = n_digits
    for i in range(k):
        ans +=  9*10**(n_digits)-increasing(n_digits)-decreasing(n_digits)+9
        #print(increasing(n_digits),decreasing(n_digits))
        n_digits -= 1
    return 10**x-1-ans
print(notBouncy(100))
t2=time.time()
print(t2-t1)
