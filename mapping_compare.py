# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:24:28 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


# compare the map of gist and pme-gist

import os

#os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/benz_mapping")
os.chdir("/Users/eric/Desktop/paper_figure/energy_compare/water/MD100ns_ref/eric.21595.master.lehman.edu/gist")

from gridData import Grid

import numpy as np

gO=Grid("gist-gO.dx").grid

coords=Grid("gist-gO.dx").edges

gist_E=Grid("gist-Eww-dens.dx").grid

pme_E=Grid("gist-Etot-pme-dens.dx").grid


gist_E_norm=np.zeros((80,80,80))
pme_E_norm=np.zeros((80,80,80))

E=[]
PME_E=[]

voxel_E=[]
voxel_PME=[]

voxel_diff=[]

diff=[]



for x in range(80):
    
    for y in range(80):
        
        for z in range(80):
            
            if gO[x,y,z] != 0:
                
                
            
                value1=gist_E[x,y,z]/(gO[x,y,z]*0.03288)
                
                voxel_energy1=gist_E[x,y,z]*0.125
                
                voxel_energy2=pme_E[x,y,z]*0.125
                
            
           
            
                value2=pme_E[x,y,z]/(gO[x,y,z]*0.03288)
                
                diff.append(value1-value2)
                
                E.append(value1)
                
                PME_E.append(value2)
            
            
                if value1 > -8.34 and value1 !=0:
                
                    gist_E_norm[x,y,z]=1
            
                if value2 > -8.34 and value2 != 0:
                
                    pme_E_norm[x,y,z]=1

Grid(gist_E_norm,edges=coords).export("high_gist_E.dx")

Grid(pme_E_norm,edges=coords).export("high_pme_E.dx")            
            

import matplotlib.pyplot as plt

plt.scatter(E,PME_E,s=2)   


X=[i for i in np.arange(-14,-2,1)]

plt.plot(X,X,color="red")

plt.xlim(-14, -2)
plt.ylim(-14, -2) 
plt.xlabel("GIST")
plt.ylabel("PME-GIST")
plt.savefig("Etot_norm_PME_GIST_GIST_compare.png", dpi=400)

plt.show()
    
            

np.mean([abs(i) for i in diff])


plt.hist(diff,bins=200,normed=True)

percentage=[100 * diff[i]/E[i] for i in range(len(E))]

np.mean([abs(i) for i in percentage])

np.mean(percentage)

plt.hist(percentage,bins=200,normed=True)