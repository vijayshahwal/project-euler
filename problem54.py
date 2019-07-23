from collections import OrderedDict
lis=[]
for i in range(int(input())):
    x=[str(x) for x in input().split()]
    lis.append(x)
d={'T':10,'J':11,'Q':12,'K':13,'A':14}
d1={'T','J','Q','K','A'}
cot=0
for i in lis:
    value1=[]
    suit1=[]
    value2=[]
    suit2=[]
    x=0
    for j in i:
        if(x<5):
            value1.append(j[0])
            suit1.append(j[1])
        else:
            value2.append(j[0])
            suit2.append(j[1])
        x+=1
    for r in range(5):
        if(value1[r] in d1):
            value1[r]=d[value1[r]]
        else:
            value1[r]=int(value1[r])
        if(value2[r] in d1):
            value2[r]=d[value2[r]]
        else:
            value2[r]=int(value2[r])
    value1=sorted(value1,reverse=True)
    value2=sorted(value2,reverse=True)
    #print(value1,end=" ")
    #print(suit1)
    #print(value2,end=" ")
    #print(suit2)
    while(True):
        #Royal Flush1
        if(set(suit1)=={suit1[0]} and value1[0]==14):
            if(value1[0]==value1[1]+1 and value1[1]==value1[2]+1 and value1[2]==value1[3]+1
               and value1[3]==value1[4]+1):
                cot+=1
                #print("Royal Flush player 1")
                break
        #Royal Flush2
        if(set(suit2)=={suit2[0]} and value2[0]==14):
            if(value2[0]==value2[1]+1 and value2[1]==value2[2]+1 and value2[2]==value2[3]+1
               and value2[3]==value2[4]+1):
                #print("Royal Flush player 2")
                break
        #straight flush1
        if(set(suit1)=={suit1[0]} and value1[0]!=14):
            if((value1[0]==value1[1]+1 and value1[1]==value1[2]+1 and value1[2]==value1[3]+1
               and value1[3]==value1[4]+1 )and value1>value2):
                cot+=1
                #print("straight Flush player 1")
                break
        #straight flush2
        if(set(suit2)=={suit2[0]} and value2[0]!=14):
            if(value2[0]==value2[1]+1 and value2[1]==value2[2]+1 and value2[2]==value2[3]+1
               and value2[3]==value2[4]+1 and value2>value1):
                #print("straight Flush player 2")
                break
        cnt11=OrderedDict()
        cnt22=OrderedDict()
        ss1=sorted(set(value1),reverse=True)
        ss2=sorted(set(value2),reverse=True)
        for k in ss1:
            cnt11[k]=value1.count(k)
        for k in ss2:
            cnt22[k]=value2.count(k)
        cnt1=list(cnt11.values())
        cnt2=list(cnt22.values())
        #print(cnt1)
        #print(cnt2)
        #four of a kind1
        if(max(cnt1)==4 and max(cnt2)!=4):
            cot+=1
            #print("four of a kind player1")
            break
        #four of a kind2
        if(max(cnt2)==4 and max(cnt1)!=4):
            #print("four of a kind player2")
            break
        #four of a kind1
        if(max(cnt1)==4 and max(cnt2)==4):
            for z in cnt11:
                if(cnt11[z]==4):
                    val=z
                    break
            for z in cnt22:
                if(cnt22[z]==4):
                    val1=z
                    break
            if(val>val1):
                cot+=1
                #print("four of a kind player 1")
                break
            if(val1>val):
                #print("four of a kind player 2")
                break
            if(val==val1 and value1>value2):
                cot+=1
                #print("four of a kind player1")
                break
            if(val==val1 and value2>value1):
                #print("four of a kind player2")
                break
        #full house1 :: three of a kind and a pair1
        if((max(cnt1)==3 and min(cnt1)==2 and len(set(cnt1))==2) and (max(cnt2)==3
            and min(cnt2)==2 and len(set(cnt2))==2)):
            for z in cnt11:
                if(cnt11[z]==3):
                    val=z
                    break
            for z in cnt22:
                if(cnt22[z]==3):
                    val1=z
                    break
            if(val>val1):
                cot+=1
                #print("full house player 1")
                break
            if(val==val1 and value1>value2):
                co+=1
                #print("Full house player 1")
                break
            if(val==val1 and value2>value1):
                #print("Full house player 2")
                break
            if(val1>val):
                #print("Full house player 2")
                break
        #full house :: three of a kind and a pair
        if((max(cnt1)==3 and min(cnt1)==2 and len(set(cnt1))==2) and (max(cnt2)<33
            or min(cnt2)<2 or len(set(cnt2))<2)):
            cot+=1
            #print("full house player 1")
            break
        #flus1 :: all cards of same suit
        if((set(suit1)=={suit1[0]} and len(set(suit1))==1) and
            (set(suit2)=={suit2[0]} and len(set(suit2))==1)):
            if(value1>value2):
                cot+=1
                #print("flush player 1")
                break
            if(value2>value1):
                #print("Flush player 2")
                break
        if(set(suit1)=={suit1[0]} and len(set(suit1))==1 and len(set(suit2))!=1):
            cot+=1
            #print("flush player 1")
            break
        if(set(suit2)=={suit2[0]} and len(set(suit2))==1 and len(set(suit1))!=1):
            #print("flush player 2")
            break
        #straight1 :: all cards of consequtive value
        if((value1[0]==value1[1]+1 and value1[1]==value1[2]+1 and value1[2]==value1[3]+1 and value1[3]==value1[4]+1)
           and not (value2[0]==value2[1]+1 and value2[1]==value2[2]+1 and value2[2]==value2[3]+1 and value2[3]==value2[4]+1)):
            cot+=1
            #print("straight player 1")
            break
        if((value2[0]==value2[1]+1 and value2[1]==value2[2]+1 and value2[2]==value2[3]+1 and value2[3]==value2[4]+1)
           and not (value1[0]==value1[1]+1 and value1[1]==value1[2]+1 and value1[2]==value1[3]+1 and value1[3]==value1[4]+1)):
            #print("straight player 2")
                break
        if((value1[0]==value1[1]+1 and value1[1]==value1[2]+1 and value1[2]==value1[3]+1 and value1[3]==value1[4]+1)
           and (value2[0]==value2[1]+1 and value2[1]==value2[2]+1 and value2[2]==value2[3]+1 and value2[3]==value2[4]+1)):
            if(value1>value2):
                co+=1
                break
            if(value2>value1):
                break
            
    
        #Three of kind1 :: three card of same value
        if(max(cnt1)==3 and max(cnt2)<3):
            cot+=1
            #print("Three of kind player1")
            break
        if(max(cnt1)==3 and max(cnt2)==3):
            for z in cnt11:
                if(cnt11[z]==3):
                    val=z
                    break
            for z in cnt22:
                if(cnt22[z]==3):
                    val1=z
                    break
            if(val>val1):
                cot+=1
                #print("Three of kind player 1")
                break
            if(val1>val):
                #print("Three of kind player2")
                break
            if(val==val1 and value1>value2):
                cot+=1
                #print("Three of kind player1")
                break
            if(val==val1 and value2>value1):
                #print("Three of kind player2")
                break
        #Three of kind2 :: three card of same value
        if(max(cnt2)==3 and max(cnt1)<3):
            #print("Three of kind player2")
            break
        #Two pair1 :: two different pairs
        if(max(cnt1)==2 and max(cnt2)<2 and cnt1.count(2)==2):
            cot+=1
            #print("Two pair player 1")
            break
        if(max(cnt1)==2 and max(cnt2)==2):
            if(cnt1.count(2)==2 and cnt2.count(2)==2):
                val=0
                val1=0
                for z in cnt11:
                    if(cnt11[z]==2):
                        val=max(z,val)
                for z in cnt22:
                    if(cnt22[z]==2):
                        val1=max(z,val1)
                        break
                if(val>val1):
                    cot+=1
                    #print("Two pair player 1")
                    break
                if(val1>val):
                    #print("Two pair player 2")
                    break
                if(val==val1 and value1>value2):
                    #print("Two pair player 1")
                    cot+=1
                    break
                if(val==val1 and value2>value1):
                    #print("Two pair player 2")
                    break
            if(cnt1.count(2)==2 and cnt2.count(2)!=2):
                cot+=1
                break
            if(cnt1.count(2)!=2 and cnt2.count(2)==2):
                break
            
        #Two pair2 :: two different pairs
        if(max(cnt2)==2 and max(cnt1)<2 and cnt2.count(2)==2):
            #print("Two pair player 2")
            break
        #one pair1 :: two cards of same value
        if(max(cnt1)==2 and max(cnt2)<2):
            cot+=1
            #print("one pair player1")
            break
        if(max(cnt2)==2 and max(cnt1)<2):
            #print("one pair player2")
            break
        if((max(cnt1)==2 and max(cnt2)==2) and cnt1.count(2)<=1):
            for z in cnt11:
                if(cnt11[z]==2):
                    val=z
                    break
            for z in cnt22:
                if(cnt22[z]==2):
                    val1=z
                    break
            if(val>val1):
                cot+=1
                #print("one pair player 1")
                break
            if(val1>val):
                #print("one pair player2")
                break
            if(val==val1 and value1>value2):
                cot+=1
                #print("one pair player 1")
                break
            if(val==val1 and value2>value1):
                #print("one pair player 2")
                break
        #Highest card1
        if(value1>value2):
            cot+=1
            #print("Highest card player1")
            break
        #Highest card2
        if(value2>value1):
            #print("Highest card player2")
            break
print(cot)            




    
