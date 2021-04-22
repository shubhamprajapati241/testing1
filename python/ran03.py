# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:58:57 2021

@author: Jam Ztudioz
"""

# random no generation by head and tail method
from numpy import random
import math
#import matplotlib.pyplot as plt
#x=random.binomial(n=100,p=0.5,size=5)
listx=[]
listy=[]
for y in range(1,100000):
    y=random.random()
    x=math.sin(math.y)
    z=round(x,3)
  #  listx.append(str(y))
   # listy.append(str(z))
#print(listx)
#print(listy)
    y=str(y)
    z=str(z)
    file_x=open("f_x01.txt","a")
    file_x.write(y +"\n")
    file_y=open("f_y01.txt","a")
    file_y.write(z +"\n")
file_x.close()
file_y.close()  
  
#plt.plot(listx,listy)
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.title("graph")
#plt.show()