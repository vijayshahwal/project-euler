#!/bin/python3

import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(l, b):
            if(l==b):
                        return(1)
            temp=l*b
            size=[ ]
            t1=1*1
            for i in range(2,l):
                        for j in range(2,b):
                                    if(i==j and temp%(i*j)==0):
                                                t2=i*j
                                                if(t2>t1 and temp%t2==0):
                                                            t1=t2
                                                            size.append(temp/(i*j)
                        print(size)
            return(max(size))

t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)
