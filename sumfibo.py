#!/usr/bin/env python 

'''Find sum of all Fibonacci numbers which are even. The numbers should not exceed 4 million and start with 1, 2 as first two fibo numbers '''

def fibo(f1,f2):
      sum=f2
      while(f2 <= 4000000):
         temp=f2
         f2=f1+f2
         f1=temp 
         if f2 % 2==0:
           sum=sum+f2 
      return sum 


if __name__=="__main__":
     print fibo(1,2)
