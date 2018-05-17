# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:53:52 2018

@author: roopal jain

"""
# taking input of elements and form a matrix
import numpy as np
p = []
num = int(input("take an integer = "))
if num == 1:
    print("cant take")
if num >1:
    for l in range(2,num):
        if(num%l) == 0:
            print("num is not prime no")
            print(l,"and",num//l,"is",num)
            break
else:
     print("num is prime no.")
if num%l == 0:       
    for i in range(2,num+2):
        m = int(input("take elements in matrix ="))
        i = i+1

        p.append(m)
        print(p)
arr = np.array(p)        
       
b=[]


for i in range(2,num):
	if num%i == 0:
        	x = int(num/i)
        	a= (arr.reshape(i,x))
        	print(a)
        

        


	


#%%               



























    
