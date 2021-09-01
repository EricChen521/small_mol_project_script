#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:43:57 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# compare the direct, reciprol and self-term to GIST energy

import os

os.chdir("/Users/eric/Desktop/paper_figure/energy_compare/water/MD100ns_ref/eric.21595.master.lehman.edu/gist")

file=open("nohup.out")

GIST_vdw=[]

GIST_elec=[]

PME_elec_dir=[]
PME_elec_cor=[]
PME_elec_rec=[]

PME_vdw_dir=[]
PME_vdw_cor=[]


for line in file:
    
    if "GIST elec_energy" in line:
        
        temp=line.split()
        
        GIST_elec.append(float(temp[4].split(",")[0]))
        
        GIST_vdw.append(float(temp[-1]))
        
    if "E_elec_self_sum" in line:
        
        temp=line.split()
        
        PME_elec_cor.append(float(temp[1].split(",")[0]))
        
        PME_elec_dir.append(float(temp[4].split(",")[0]))
        
        PME_elec_rec.append(float(temp[7].split(",")[0]))
        
        PME_vdw_dir.append(float(temp[10].split(",")[0]))
        
        PME_vdw_cor.append(float(temp[-1]))
        
        

sum(GIST_elec)/50000

sum(GIST_vdw)/50000


sum(PME_elec_dir)/50000
sum(PME_elec_rec)/50000
sum(PME_elec_cor)/50000


sum(PME_vdw_dir)/50000

sum(PME_vdw_cor)/50000


GIST_elec[0]

PME_elec_dir[0]+PME_elec_rec[0]+PME_elec_cor[0]


PME_elec=[PME_elec_dir[i]+PME_elec_rec[i]+PME_elec_cor[i] for i in range(50000)]

PME_vdw=[PME_vdw_dir[i]+PME_vdw_cor[i] for i in range(50000)]

X=[i for i in range(50000)]

len(X)

diff_elec=[GIST_elec[i]-PME_elec[i] for i in range(50000)]

diff_vdw=[GIST_vdw[i]-PME_vdw[i] for i in range(50000)]

diff_total=[diff_elec[i]+diff_vdw[i] for i in range(50000)]

import matplotlib.pyplot as plt

#plt.plot(X,diff_total,"black",label="E_total diff(GIST-PME)")

#plt.scatter(X,PME_elec,"green",label="PME elec")

#plt.hist(diff_total,bins=100,label="E_total diff(GIST-PME")

#plt.hist(diff_elec,bins=100,color="red",label="elec diff(GIST-PME")

plt.hist(diff_vdw,bins=100,color="orange",label="vdw diff(GIST-PME")


plt.legend()

plt.show()



        
        
        
        
        
        
        

        
        
    
    
    
