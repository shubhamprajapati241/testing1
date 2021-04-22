# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:25:54 2021

@author: Jam Ztudioz
"""
mylist=[]
import numpy 
from numpy import random
for i in range(1,100):    
    i=random.random()
    y=round(i,3)
    y_str = str(y)
    f = open("ran01.txt","a")
    f.write(y_str+"\n")
f.close()

    