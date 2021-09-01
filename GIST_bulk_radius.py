#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:46:34 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# the the Eww depending on the radius

import os

os.chdir("/Users/eric/Desktop/paper_figure/energy_compare/water/MD100ns_ref/eric.21595.master.lehman.edu/gist")


data=open("gist-output.dat").readlines()

from gridData import Grid

import numpy as np

import glob



position=[]

for x in range(80):
    
    for y in range(80):
        
        for z in range(80):
            
            position.append((x,y,z))
            
            
PME_dens=np.zeros((80,80,80))
    
#TSsix_dens=np.zeros((60,60,60))
    
Population=np.zeros((80,80,80))
    
Eww_dens=np.zeros((80,80,80))
    
#Esw_dens=np.zeros((60,60,60))     

       
voxel=0
        
for line in data[2:]:
        
    temp=line.split()
        
    #voxel_coord=[float(temp[1]),float(temp[2]),float(temp[3])]
        
        
        
        
    #TSsix_temp=float(temp[11])
    E_dens_temp=float(temp[17])
    
    pop_temp=float(temp[4])
        
    Eww_temp=float(temp[15])
    
    #Esw_temp=float(temp[13])
        
    PME_dens[position[voxel]]=E_dens_temp
        
    Eww_dens[position[voxel]]=Eww_temp
        
    #Esw_dens[position[voxel]]=Esw_temp
        
    #TSsix_dens[position[voxel]]=TSsix_temp
    Population[position[voxel]]=pop_temp/50000
        
    voxel+=1
    
    
np.sum(PME_dens)

np.sum(Eww_dens)


Ebulk_pme=[]
Ebulk_gist=[]
POP=[]




for i in range(1,15):
    
    PME_E_temp=np.sum(PME_dens[15-i:15+i,15-i:15+i,15-i:15+i])*0.125
    
    GIST_E_temp=np.sum(Eww_dens[15-i:15+i,15-i:15+i,15-i:15+i])*0.125
    
    Pop_temp=np.sum(Population[15-i:15+i,15-i:15+i,15-i:15+i])
    
    Ebulk_pme.append(PME_E_temp/Pop_temp)
    
    Ebulk_gist.append(GIST_E_temp/Pop_temp)
    
    POP.append(Pop_temp)
    
    
GIST_local=[]
PME_local=[]
Pop_local=[]

for i in range(1,15):
    
    PME_E_temp=np.sum(PME_dens[15-i:15+i,15-i:15+i,15-i:15+i])*0.125
    
    GIST_E_temp=np.sum(Eww_dens[15-i:15+i,15-i:15+i,15-i:15+i])*0.125
    
    Pop_temp=np.sum(Population[15-i:15+i,15-i:15+i,15-i:15+i])
    
    GIST_local.append(GIST_E_temp)
    PME_local.append(PME_E_temp)
    Pop_local.append(Pop_temp)
    


    


print(len(GIST_local))

Ebulk_gist_local=[(GIST_local[i+1]-GIST_local[i])/(POP[i+1]-POP[i]) for i in range(0,13)]

Ebulk_pme_local=[(PME_local[i+1]-PME_local[i])/(POP[i+1]-POP[i]) for i in range(0,13)]



X=[i for i in range(1,14)]

import matplotlib.pyplot as plt
plt.plot(X,Ebulk_pme_local,"red",label="Ebulk_pme") 
plt.plot(X,Ebulk_gist_local,"green",label="Ebulk_gist")

plt.legend()

plt.show()
    
    
                                
                                