#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:06:21 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# compare the potential energy difference calculated by GIST, PME-GIST and PMEMD-Amber

import os

os.chdir("/Users/eric/Desktop/paper_figure/water/NPT_water")

# Parse the amber energy output file

file1=open("prod.out").readlines()

Amber_E=[]

for line in file1:
    
    if "Etot" in line and "EPtot" in line:
        
        Amber_E.append(float(line.split()[-1]))

# parse the PME-GIST output file

GIST_E=[]

PME_E=[]


file2=open("/Users/eric/Desktop/paper_figure/water/NPT_water/everyframe_gist/nohup.out")


for line in file2:
    
    if "total GIST energy" in line:
        
        GIST_E.append(float(line.split()[-1]))
        
    if "total potential energy on water" in line:
        
        PME_E.append(float(line.split()[-1]))


print(len(Amber_E))

print(len(GIST_E))

print(len(PME_E))

X=[i for i in range(1,10000)]


Diff1=[PME_E[i]-Amber_E[i+1] for i in range(9999)]

Diff2=[GIST_E[i]-Amber_E[i+1] for i in range(9999)]

import matplotlib.pyplot as plt

plt.plot(X,Diff1,"black",label="PME-Amber")

plt.plot(X,Diff2,"red",label="GIST-Amber")

plt.xlabel("frame #")

plt.ylabel("Total Energy Difference in Kcal/mol")

plt.legend()

plt.savefig("PME_and_GIST_energy_diff_by_frame.png", dpi=400)

plt.show()


max(Diff1)

min(Diff1)

Diff1_average=sum(Diff1)/len(Diff1)

Diff2_average=sum(Diff2)/len(Diff2)


    
        
        