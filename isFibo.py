#!/usr/bin/env python 
'''Program to check if a number is in the Fibonacci series '''
def isFibo(n):
    root1=(5*n**2+4)**0.5 
    root2=(5*n**2-4)**0.5 
    if (root1== int(root1)) or (root2 == int(root2)):
      return "isFibo"
    else:
      return "isNotFibo"


if __name__=="__main__":
     
     t=int(raw_input())
     results=[] 
     for i in range(t):
       n=int(raw_input())
       results.append(isFibo(n))
     for r in results:
       print r    
