#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:27:12 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# Calculate the solvation free energy by end-state

import os

os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/PME-GIST")


import glob

import numpy as np

water_ref_pme=-9.5422
water_ref_gist=-9.5353



GIST_files=sorted(glob.glob("*MD*gist*dat"))

class mol:
    
    def __init__(self,name,E_ligand_self,E_ligand_pme,E_water_pme,E_water_old,TSori,TStrans,TSsix,TSsix_signal,water_num,neighbor,water_number_signal,water_num_sub_edge):
        
        self.name=name
        self.E_ligand_self=E_ligand_self
        self.E_ligand_pme=E_ligand_pme
        self.E_water_pme=E_water_pme
        self.E_water_old=E_water_old
        self.TSori=TSori
        self.TStrans=TStrans
        self.TSsix=TSsix
        self.water_num=water_num
        self.TSsix_signal=TSsix_signal
        self.neighbor=neighbor
        self.water_num_signal=water_number_signal
        self.water_num_sub_edge=water_num_sub_edge


ligand_self={}
ligand_pme={}

#print(ligand_self)

result=[]

file1=open("32_mols_ligand_self.energy").readlines()

for i in range(3,128,4):
    
    name=file1[i].strip()
    v1=float(file1[i-3])
    v2=float(file1[i-2])
    v3=float(file1[i-1])
    ligand_self.update({name:[v1,v2,v3]})
    
    
    
file2=open("32_mols_solute_half_pme.energy").readlines()

for i in range(3,128,4):
    
    name=file2[i].strip()
    v1=float(file2[i-3])
    v2=float(file2[i-2])
    v3=float(file2[i-1])
    ligand_pme.update({name:[v1,v2,v3]})
    
    

E_water={}
TSsix={}
water_num={}

position=[]

for x in range(60):
    
    for y in range(60):
        
        for z in range(60):
            
            position.append((x,y,z))

for file in GIST_files:
    
    target=file.split("_half")[0]
    
    print(target)
    
    e_water_pme=[]
    e_water_old=[]
    tssix=[]
    tsori=[]
    tstrans=[]
    pop=[]
    nei=[]
    
    
    tssix_grid=np.zeros((60,60,60))
    nei_grid=np.zeros((60,60,60))
    pop_grid=np.zeros((60,60,60))
    
    
    contents=open(file).readlines()[2:]
    
    voxel=0
    for line in contents:
        temp=line.split()
        
        #voxel=contents.index(line)
        
        
            
        tssix_grid[position[voxel]]=0.125*float(temp[11])
        nei_grid[position[voxel]]=float(temp[24])
        pop_grid[position[voxel]]=float(temp[4])/50000
        
      
        
        tsori.append(0.125*float(temp[9]))
        tstrans.append(0.125*float(temp[7]))
        tssix.append(0.125*float(temp[11]))
        e_water_old.append(0.125*(float(temp[13])+float(temp[15])))
        e_water_pme.append(0.125*float(temp[17]))
        pop.append(float(temp[4])/50000)
        nei.append(float(temp[24]))
        
        
        voxel+=1
    
    
    name=target.split("_")[0]
    replica=int(target.split("MD")[-1])-1
    
    entropy_choice=[]
    
    
    
    for d in range(31):
        
        #print(d)
        
        entropy_temp=np.sum(tssix_grid[30-d:30+d,30-d:30+d,30-d:30+d])
        entropy_choice.append(entropy_temp)
    
    d_choice=entropy_choice.index(min(entropy_choice))
    
    nei_signal=np.mean(nei_grid[30-d_choice:30+d_choice,30-d_choice:30+d_choice,30-d_choice:30+d_choice])
    
    pop_signal=np.sum(pop_grid[30-d_choice:30+d_choice,30-d_choice:30+d_choice,30-d_choice:30+d_choice])
    
    pop_sub_edge=np.sum(pop_grid[1:59,1:59,1:59]) 
    
    
        
    
    
        
    p=mol(target,ligand_self[name][replica],ligand_pme[name][replica],sum(e_water_pme),sum(e_water_old),sum(tsori),sum(tstrans),sum(tssix),
          min(entropy_choice),sum(pop),nei_signal,pop_signal,pop_sub_edge)
    
    result.append(p)
    
    
    
    
    
    
    
import xlsxwriter
workbook=xlsxwriter.Workbook("32mol_GIST_result.xlsx")
worksheet=workbook.add_worksheet()

row=1


for m in result:
    
    worksheet.write(0,1,"E_ligand_self")
    worksheet.write(0,2,"E_ligand_pme")
    worksheet.write(0,3,"E_water_pme")
    worksheet.write(0,4,"E_pme")
    worksheet.write(0,5,"E_gist")
    worksheet.write(0,6,"TSsix")
    worksheet.write(0,7,"water_num")
    worksheet.write(0,8,"TSori")
    worksheet.write(0,9,"TStrans")
    worksheet.write(0,10,"TSsix_signal")
    worksheet.write(0,11,"Average water Neighbor")
    worksheet.write(0,12,"water_num_signal")
    worksheet.write(0,13,"water_num_sub_edge")
    
    worksheet.write(row,0,m.name)
    worksheet.write(row,1,m.E_ligand_self)
    worksheet.write(row,2,m.E_ligand_pme)
    worksheet.write(row,3,m.E_water_pme)
    worksheet.write(row,4,m.E_water_pme+m.E_ligand_pme-m.E_ligand_self)
    worksheet.write(row,5,m.E_water_old)
    worksheet.write(row,6,m.TSsix)
    worksheet.write(row,7,m.water_num)
    worksheet.write(row,8,m.TSori)
    worksheet.write(row,9,m.TStrans)
    worksheet.write(row,10,m.TSsix_signal)
    worksheet.write(row,11,m.neighbor)
    worksheet.write(row,12,m.water_num_signal)
    worksheet.write(row,13,m.water_num_sub_edge)
    
    row=row+1
    
    
col=1
for i in range(0,len(result),3):
    
    name=result[i].name.split("_")[0]
    
    Enthalpy=0
    Entropy_TSsix=0
    Entropy_TSsix_signal=0
    Enthalpy_old=0
    Water_NUM=0
    

    
    for j in range(i,i+3):
        
    
        Enthalpy += result[j].E_water_pme + result[j].E_ligand_pme - result[j].E_ligand_self - (result[j].water_num * water_ref_pme)
        
        Entropy_TSsix += result[j].TSsix
        
        Entropy_TSsix_signal += result[j].TSsix_signal
        
        Enthalpy_old += result[j].E_water_old - (result[j].water_num * water_ref_gist)
        
        Water_NUM +=result[j].water_num
    
    worksheet.write(row+2,0,"compound")
    
    worksheet.write(row+2,col,name)
    
    worksheet.write(row+3,0,"Average dH pme")
    
    
    worksheet.write(row+3,col,Enthalpy/3)
    
    worksheet.write(row+4,0,"Average TSsix")
    worksheet.write(row+4,col,Entropy_TSsix/3)
    
    worksheet.write(row+5,0,"Average TSsix_signal")
    worksheet.write(row+5,col,Entropy_TSsix_signal/3)
    
    worksheet.write(row+6,0,"Average dH old")
    
    worksheet.write(row+6,col,Enthalpy_old/3)
    
    worksheet.write(row+7,0,"Average Water Num")
    worksheet.write(row+7,col,Water_NUM/3)
    
    col+=1

workbook.close()
    

# filter the noise by the minium TSsix




    
#print(entropy_choice)
    
       
        
        


   
    

