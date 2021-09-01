# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:02:38 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


# fitting the high order entropy 


import os

os.chdir("D:/eric/Entropy_esti/15_mols")

import matplotlib.pyplot as plt

import statistics as stat



# check the distribution of TSsix of pure water

#colume 11 TSsix dens, 24, Neighbor-norm. 4 pop

file0=open("tip3p_pure_water_gist-output.dat").readlines()[2:]

Neighbor_norm=[]
TSsix=[]
pop=[]

for line in file0:
    
    if float(line.split()[11]) !=0:
        
    
        Neighbor_norm.append(float(line.split()[24]))
        TSsix.append(0.125*float(line.split()[11]))
        pop.append(float(line.split()[4])/50000)


sum(TSsix)

stat.stdev(Neighbor_norm)
stat.mean(Neighbor_norm)

Neigh_uplimit= stat.mean(Neighbor_norm)+ 3* stat.stdev(Neighbor_norm)

Neigh_lowlimit= stat.mean(Neighbor_norm)- 3* stat.stdev(Neighbor_norm)


S_uplimit = stat.mean(TSsix) + 3 * stat.stdev(TSsix)

S_lowlimit = stat.mean(TSsix) - 3 * stat.stdev(TSsix)

stat.stdev(TSsix)
stat.mean(TSsix)

sum(pop)

TSsix[0]

plt.hist(Neighbor_norm,bins=50)

max(Neighbor_norm)

t=Neighbor_norm.index(5.67797)

TSsix[t]

signal_TS_total=[]
signal_pop=[]


for i in range(len(TSsix)):
    
    if Neighbor_norm[i] < Neigh_lowlimit or Neighbor_norm[i] > Neigh_uplimit:
        
        S_total = (1 + (Neighbor_norm[i]/5.2564)) * TSsix[i]
        
        signal_TS_total.append(S_total)
        
        signal_pop.append(pop[i])
        
    
sum(signal_TS_total)

sum(signal_pop)


# play with benzene

print("S_uplimit: {0}; S_lowlimit: {1} \n".format(S_uplimit, S_lowlimit))
file1=open("benzene_MD1_full_energy_gist-output.dat").readlines()[2:]

benz_neighb=[]

benz_pop=[]

benz_TSsix=[]

benz_TS_all=[]

for line in file1:
    
    temp=line.split()
    
    if 0.125 * float(temp[11]) < S_lowlimit or 0.125 *float(temp[11]) > S_uplimit:
        
        benz_TSsix.append(0.125 * float(temp[11]))
        benz_pop.append(float(temp[4])/50000)
        benz_neighb.append(float(temp[24]))
        
        #fac = float(temp[24]) / 5.25 
        
        
        
        
        
sum(benz_TSsix)

sum(benz_neighb)


sum(benz_pop)    

stat.mean(benz_neighb)

factor = sum(benz_neighb)/(5.25 * len(benz_neighb))  



print(factor)

delta_S= sum(benz_TSsix)/(1-factor) - sum(benz_pop) * (-3.47)


    
    
    




