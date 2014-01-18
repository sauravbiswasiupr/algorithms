#!/usr/bin/env python 
'''Program to find the difference between Square of sum and sum of squares of n numbers'''

def findsumsqdiff(n):
     sum=0
     sqsum=0
     for i in range(1,n+1):
        sum+=i 
        sqsum+=i**2
     return abs(sum**2-sqsum)


if __name__=="__main__":
     print findsumsqdiff(100)
