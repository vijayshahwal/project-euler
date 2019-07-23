from collections import OrderedDict
def numToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy',
            'eighty','ninety']
    thousands = ['','thousand']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = int((numStrLen+2)/3)
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[1]+',')
    if join: return"".join(words)
    return words
n,m = map(int,input().split())
converge=True
while(True):
    d1=dict()
    d2=dict()
    if(m==n):
        print(m)
        break
    if(converge and (n<=99999 or m<=99999)):
        d1[n]=[numToWords(n),numToWords(m)]
        d2[n]=[sorted([numToWords(n),numToWords(m)])[0],sorted([numToWords(n),numToWords(m)])[1]]
        if(d1!=d2):
            print(m+n)
            converge=False
            break
        n+=n
        m+=m
    else:
        if(converge):
            print("Out of Bounds")
        break
    
