# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:15:44 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


import os

os.chdir("D:/eric/Entropy_esti/TI_potential")

gist=open("gist_pme.out").readlines()

ti=open("ti001.out").readlines()


gist_E=[]
ti_E=[]

SW_E=[]


for line in gist:
    
    if "pme potentail energy" in line:
        
        t1=line.split(":")[1]
        t2=t1.split(",")[0]
        #print(t2)
        gist_E.append(float(t2))
    
    if "water pme" in line:
        
        SW_E.append(float(line.split()[-1]))
        

for line in ti:
    
    if "EAMBER (" in line:
        
        t=line.split()[-1]
        
        ti_E.append(float(t))
    
TI_E=[ i for i in ti_E[::2]]

len(TI_E)
       
import numpy as np

x=np.arange(-12500,-12380,1)

import matplotlib.pyplot as plt

plt.scatter(TI_E[0:99],gist_E[0:99],s=10)



plt.plot(x,x,color="red")

plt.xlabel("TI")
plt.ylabel("CPPTRAJ_Energy")
plt.title("System Potential Energy")

plt.show()




diff=[gist_E[i] - TI_E[i] for i in range(99)]

#print(diff)

average=sum(diff)/len(diff)


ss=[gist_E[i] - SW_E[i] for i in range(len(SW_E))]

print(ss)


    
        
        

