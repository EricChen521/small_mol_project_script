#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:08:41 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# compare the voxel energy of bulk water by GIST and by PME

import os

#os.chdir("/Users/eric/Desktop/paper_figure/gist")

os.chdir("/Users/eric/Desktop/paper_figure/energy_compare/water/MD100ns_ref/eric.21595.master.lehman.edu/gist")

file=open("gist-output.dat").readlines()[2:]

GIST_E=[]

PME_E=[]

TSsix=[]

diff_percentage=[]

DIFF=[]

for line in file:
    
    temp=line.split()
    
    if float(temp[15])!=0:
        
    
        GIST_E.append(float(temp[15]))
        PME_E.append(float(temp[17]))
        
        TSsix.append(float(temp[11]))
    
        diff=PME_E[-1]-GIST_E[-1]
        
        if diff==0:
            
            print("same")
    
        diff_percentage.append(diff/GIST_E[-1])
        
        DIFF.append(diff)
        
        
        

        
import matplotlib.pyplot as plt



sum(TSsix)





import numpy as np

X=np.arange(-0.5,0.2, 0.1)

plt.scatter(GIST_E,PME_E,s=5)

plt.plot(X,X,"r--")

plt.xlabel("Energy density by GIST-2016, Kcal/mol/A3")

plt.ylabel("Energy density by PME-GIST, Kcal/mol/A3")

plt.xticks(X)

plt.yticks(X)



plt.savefig("voxel_water_energy.png",dpi=400)

plt.show()



len(PME_E)

import statistics as stats

stats.mean(PME_E)
stats.stdev(PME_E)

stats.mean(GIST_E)

stats.stdev((GIST_E))


DIFF_percentage=[i for i in diff_percentage if abs(i)<0.03]

plt.hist(DIFF_percentage,bins=100,density=True)

plt.ylabel("Normalized frequceny")
plt.xlabel("Relative difference of energy density")

plt.savefig("voxel_water_energy_change_percentage",dpi=400)
plt.show()

plt.hist(DIFF,bins=200,density=True)



sum(GIST_E)*0.125

sum(PME_E)*0.125

abs_diff_per=[abs(i) for i in diff_percentage]

abs_mean_diff=sum(abs_diff_per)/len(abs_diff_per)

print(abs_mean_diff)


majority=[i for i in abs_diff_per if i <= 0.02]

print(len(abs_diff_per))

print(len(majority))

print(len(majority)/len(abs_diff_per))

print(abs_mean_diff)


# for whole 32 solute-water system,cample the relative voxel energy difference


os.chdir("/Users/eric/Desktop/paper_figure/whole_system_gist")

import glob

files=sorted(glob.glob("*MD1*dat"))

print(files)

Mean_diff_per=[]



for f in files[:1]:
    
    print(f)
    
    dat=open(f).readlines()[2:]
    
    GIST_E=[]
    PME_E=[]
    diff_percentage=[]
    
    for line in dat:
        
        #print("haha")
        
        temp=line.split()
        
        if float(temp[15])!=0:
            
            #print("KAK")
        
    
            GIST_E.append(float(temp[15])+0.5*float(temp[13]))
            PME_E.append(float(temp[17]))
    
            diff=PME_E[-1]-GIST_E[-1]
            
            #print(diff)
            
            
        
    
            diff_percentage.append(diff/GIST_E[-1])
            
            Mean_diff_per.append(stats.mean(diff_percentage))
            
print(Mean_diff_per)   


GIST_Esw_files=sorted(glob.glob("*MD1*Esw*dx"))

GIST_Eww_files=sorted(glob.glob("*MD1*Eww*dx"))

PME_E_files=sorted(glob.glob("*MD1*pme*dx"))

len(GIST_Eww_files)


import numpy as np

from gridData import Grid


diff_targets=[]

old_err_state=np.seterr(divide='raise')


for i in range(32):
    
    GIST_voxel_E=np.add(Grid(GIST_Eww_files[i]).grid,0.5*Grid(GIST_Esw_files[i]).grid)
    
    PME_voxel_E=Grid(PME_E_files[i]).grid
    
    voxel_diff_grid=np.subtract(PME_voxel_E, GIST_voxel_E)
    
    ignored_states=np.seterr(**old_err_state)
    
    diff_per_grid=np.divide(voxel_diff_grid, GIST_voxel_E)
    
    diff_per_grid[~np.isfinite(diff_per_grid)]=0
    
    
    
    t=np.sum(np.absolute(diff_per_grid))/np.count_nonzero(diff_per_grid)
    
    print(t)
    
    diff_targets.append(t)
    
    
    
print(sum(diff_targets)/32)

ignored_states = np.seterr(**old_err_state)

np.divide(1,0)

        
        
        