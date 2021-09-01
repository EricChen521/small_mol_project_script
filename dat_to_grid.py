# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:02:41 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


# read the gist dat output file and transform it to ndarray
import os

os.chdir("D:/eric/Entropy_esti/15_mols/half_energy") 

import glob

import numpy as np

files=sorted(glob.glob("*MD1*dat"))
A={}  # dictory for {name:(entropy, energy, polulation)}

position=[]

for x in range(60):
    
    for y in range(60):
        
        for z in range(60):
            
            position.append((x,y,z))



for file in files[0:1]:
    
    
    
    E_dens=np.zeros((60,60,60))
    
    TSsix_dens=np.zeros((60,60,60))
    
    Population=np.zeros((60,60,60))
    
    data=open(file).readlines()[2:]
    
    
    
    for line in data:
        
        voxel=data.index(line)
        
        TSsix_temp=float(line.split()[11])
        
        E_dens_temp=float(line.split()[17])
        
        pop_temp=float(line.split()[4])
        
        
        E_dens[position[voxel]]=E_dens_temp
        
        TSsix_dens[position[voxel]]=TSsix_temp
        
        Population[position[voxel]]=pop_temp
        
        if voxel % 200000 == 0:
            
            print(file)
            
    Entropy_choice=[]
    
    Energy_choice=[]
    
    Pop_choice=[]
    
    for i in range(31):
        
        temp1=np.sum(0.125*TSsix_dens[30-i:30+i,30-i:30+i,30-i:30+i])
        
        Entropy_choice.append(temp1)
        
        temp2=np.sum(0.125*E_dens[30-i:30+i,30-i:30+i,30-i:30+i])
        
        Energy_choice.append(temp2)
        
        temp3=np.sum(Population[30-i:30+i,30-i:30+i,30-i:30+i])/50000
        
        Pop_choice.append(temp3)
        
        print("within GRID size: {0}; water energy: {1}; entropy: {2}; water num:{3} \n".format(i, temp2,temp1,temp3))
        
        #dE = temp2 - (-9.5422381) * temp3
        
        #dTS = 0.5 * temp1
        
        #dG = dE - dTS
        
        #print("within GRID size: {0}; water dE: {1}; dTS: {2}; dG: {3} \n".format(i, dE, dTS, dG))
        
        
    Entropy_signal=min(Entropy_choice)
    
    size=Entropy_choice.index(Entropy_signal)
    
    #Energy_signal=np.sum(E_dens[30-size:30+size,30-size:30+size,30-size:30+size])
    
    Population_signal=np.sum(Population[30-size:30+size,30-size:30+size,30-size:30+size])/50000
    
    name=file.split("_half")[0]    
    
    #A.update({name:(0.125*Entropy_signal,0.125*Energy_signal,Population_signal)})
    
    print("Name: {0}; whole GRID water energy: {1}; whole GRID water num: {2}; signal TSsix entropy: {3} with dimension size {4} A; water num within signal grid: {5} \n".format(name,0.125*np.sum(E_dens),np.sum(Population)/50000,Entropy_signal,size,Population_signal))
    
    #dE=0.125*np.sum(E_dens) - np.sum(Population)* (-9.5422381)/50000
    
    #d_TS=0.5 * 0.125*Entropy_signal
    
    #dG = dE - d_TS
    
    #print("Name: {0}; dE: {1}; dTS: {2}; dG: {3} \n".format(name,dE,d_TS,dG))
    
        
#np.sum(Population/50000)
#np.sum(0.125*E_dens)
#np.sum(0.125*TSsix_dens)

#print(Entropy_choice)

#print(A["acetamide_MD1"])         
            
        
        
        
        
    
    
    
    
    
    




