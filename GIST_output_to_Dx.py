#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:53:30 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# extract the water PME half energy, TSsix, population

import os

#os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/PME-GIST")


from gridData import Grid

import numpy as np

import glob


dat_files=glob.glob("*.dat")

position=[]

for x in range(60):
    
    for y in range(60):
        
        for z in range(60):
            
            position.append((x,y,z))

for f in dat_files:
    
    """
    
    ligand_file=open(f.split("half")[0]+"prod.pdb").readlines()
    
    ligand_atom_coordinates=[]
    
    for l in ligand_file:
        
        content=l.split()
        
    
        if "ATOM" in content and content[-1]!="H":
            
            coordinate=(float(content[5]),float(content[6]),float(contents[7]))
            
            ligand_atom_coordinates.append(coordinate)
    
    
    """
    voxel=0
    

    
    E_dens=np.zeros((60,60,60))
    
    TSsix_dens=np.zeros((60,60,60))
    
    Population=np.zeros((60,60,60))
    
    Eww_dens=np.zeros((60,60,60))
    
    Esw_dens=np.zeros((60,60,60))
    
    
    data=open(f).readlines()[2:]
    
    x_start=float(data[0].split()[1])-0.5
    y_start=float(data[0].split()[2])-0.5
    z_start=float(data[0].split()[3])-0.5
    
    x_end=float(data[-1].split()[1])+1
    y_end=float(data[-1].split()[2])+1
    z_end=float(data[-1].split()[3])+1
    
    x_array=np.arange(x_start,x_end,0.5)
    y_array=np.arange(y_start,y_end,0.5)
    z_array=np.arange(z_start,z_end,0.5)
    
    coordinates=[x_array,y_array,z_array]
    
 
    
    
    
    
    for line in data:
        
        temp=line.split()
        
        voxel_coord=[float(temp[1]),float(temp[2]),float(temp[3])]
        
        
        
        
        TSsix_temp=float(temp[11])
        E_dens_temp=float(temp[17])
        pop_temp=float(temp[4])
        
        Eww_temp=float(temp[15])
        Esw_temp=float(temp[13])
        
        E_dens[position[voxel]]=E_dens_temp
        
        Eww_dens[position[voxel]]=Eww_temp
        
        Esw_dens[position[voxel]]=Esw_temp
        
        TSsix_dens[position[voxel]]=TSsix_temp
        Population[position[voxel]]=pop_temp/50000
        
        voxel+=1
        
    Grid(grid=E_dens,edges=coordinates).export(f.split("half")[0]+"PME_E_dens.dx")
    
    Grid(grid=Eww_dens,edges=coordinates).export(f.split("half")[0]+"GIST_Eww_dens.dx")
    
    Grid(grid=Esw_dens,edges=coordinates).export(f.split("half")[0]+"GIST_Esw_dens.dx")
    
    Grid(grid=TSsix_dens,edges=coordinates).export(f.split("half")[0]+"TSsix_dens.dx")
    
    Grid(grid=Population,edges=coordinates).export(f.split("half")[0]+"population.dx")
    





#c=Grid("Etot-dens_6JYT_APO_rigid.dx").edges


    
    
            
#np.arange(0.5,2,0.5)           
        
        