# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 08:23:59 2021

@author: Jam Ztudioz
"""

# program for cummutative probability density
import numpy as np
import matplotlib.pyplot as plt
#from numpy import random
#import math
list_x=[]
list_y=[]
for i in range(1,10):
    y=np.random.uniform(0,1)
    y=round(y,4)
    y=str(y)
    i=str(i)
    list_x.append(i)
    list_y.append(y)
    plt.plot(list_x,list_y)
    plt.xlabel("Number")
    plt.ylabel("Uniform Random no")
    plt.title("graph")
    plt.show()
    
    #fy=open("randomy.txt","a")
    #fy.write(y+"\n")
    #fy.write(i+"\n")
#fy.close()