def palindrome(n):
        st = str(n)
        t=st[::-1]
        if(st==t):
                return True
        return False
print(palindrome(1))
