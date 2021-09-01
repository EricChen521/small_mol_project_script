#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:59:16 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

import os

os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/Tip3p_bulk")

import numpy as np

from gridData import Grid


TSsix=0.125*Grid("gist-dTSsix-dens.dx").grid

TSsix.shape

file=open("gist-output.dat").readlines()[2:]

pop_grid=np.zeros((56,56,55))

position=[]

for x in range(56):
    
    for y in range(56):
        
        for z in range(55):
            
            position.append((x,y,z))
            
voxel=0

for line in file:
    
    temp=line.split()
    
    pop_grid[position[voxel]]=float(temp[4])/50000
    voxel+=1

np.sum(pop_grid) # water number of GIST grid

np.sum(pop_grid[1:55,1:55,1:54])


    
    
    
    


np.sum(TSsix)

import matplotlib.pyplot as plt

non_zero=[i for i in list(TSsix.ravel()) if i != 0]

plt.hist(non_zero,bins=100)

plt.ylabel("Frequency")
plt.xlabel("TSsw of the voxel in Kcal/mol")

plt.savefig("TSsix_bulk.png", dpi=400)

plt.show()


