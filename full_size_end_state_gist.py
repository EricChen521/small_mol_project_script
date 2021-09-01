#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:47:00 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# full size end state gist

import os

os.chdir("/Users/eric/Desktop/paper_figure/whole_system_gist")

import glob

import numpy as np

from gridData import Grid

from scipy import stats

water_ref_pme=-9.5422
water_ref_gist=-9.5353



GIST_files=sorted(glob.glob("*MD*gist*dat"))

class mol:
    
    def __init__(self,name,E_ligand_self,E_ligand_pme,E_water_pme,E_water_old,TSsix,water_num):
        
        self.name=name
        self.E_ligand_self=E_ligand_self
        self.E_ligand_pme=E_ligand_pme
        self.E_water_pme=E_water_pme
        self.E_water_old=E_water_old
     
        self.TSsix=TSsix
        self.water_num=water_num
       
        

ligand_self={}
ligand_pme={}

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
    
    
position=[]

for x in range(100):
    
    for y in range(100):
        
        for z in range(100):
            
            position.append((x,y,z))

for file in GIST_files:
    
    target=file.split("_gist")[0]
    
    print(target)
    
    e_water_pme=[]
    e_water_old=[]
    tssix=[]
   
    pop=[]
  
    
    
    tssix_grid=np.zeros((100,100,100))
    nei_grid=np.zeros((100,100,100))
    pop_grid=np.zeros((100,100,100))
    
    
    contents=open(file).readlines()[2:]
    
    
    x_start=float(contents[0].split()[1])-0.5
    y_start=float(contents[0].split()[2])-0.5
    z_start=float(contents[0].split()[3])-0.5
    
    x_end=float(contents[-1].split()[1])+1
    y_end=float(contents[-1].split()[2])+1
    z_end=float(contents[-1].split()[3])+1
    
    x_array=np.arange(x_start,x_end,0.5)
    y_array=np.arange(y_start,y_end,0.5)
    z_array=np.arange(z_start,z_end,0.5)
    
    coordinates=[x_array,y_array,z_array]
    
    voxel=0
    for line in contents:
        temp=line.split()
        
        #voxel=contents.index(line)
        
        
            
        tssix_grid[position[voxel]]=0.125*float(temp[11])
      
        pop_grid[position[voxel]]=float(temp[4])/50000
        
      
        
   
  
        tssix.append(0.125*float(temp[11]))
        
        e_water_old.append(0.125*(float(temp[13])+float(temp[15])))
        
        e_water_pme.append(0.125*float(temp[17]))
        
        pop.append(float(temp[4])/50000)
        
      
        
        
        voxel+=1
    
    
    name=target.split("_")[0]
    replica=int(target.split("MD")[-1])-1
    
    Grid(grid=pop_grid,edges=coordinates).export(target+"_population.dx")
    
    p=mol(target,ligand_self[name][replica],ligand_pme[name][replica],sum(e_water_pme),sum(e_water_old),sum(tssix),
       sum(pop))
    
    result.append(p)
    
    
    
    
    
import xlsxwriter
workbook=xlsxwriter.Workbook("32mol_GIST_result.xlsx")
worksheet=workbook.add_worksheet()

row=1


for m in result:
    
    worksheet.write(0,1,"E_ligand_self")
    worksheet.write(0,2,"E_ligand_pme")
    worksheet.write(0,3,"E_water_pme")
    worksheet.write(0,4,"E_sys_pme")
    worksheet.write(0,5,"E_sys_gist")
    worksheet.write(0,6,"TSsix")
    worksheet.write(0,7,"water_num")
    
    
    worksheet.write(row,0,m.name)
    worksheet.write(row,1,m.E_ligand_self)
    worksheet.write(row,2,m.E_ligand_pme)
    worksheet.write(row,3,m.E_water_pme)
    worksheet.write(row,4,m.E_water_pme+m.E_ligand_pme-m.E_ligand_self)
    worksheet.write(row,5,m.E_water_old)
    worksheet.write(row,6,m.TSsix)
    worksheet.write(row,7,m.water_num)
   
    
    row=row+1
    
    
col=1
for i in range(0,len(result),3):
    
    name=result[i].name.split("_")[0]
    
    Enthalpy=[]
    Entropy_TSsix=[]
 
    Enthalpy_old=[]
    Water_NUM=0
    

    
    for j in range(i,i+3):
        
    
        Enthalpy.append(result[j].E_water_pme + result[j].E_ligand_pme - result[j].E_ligand_self - (result[j].water_num * water_ref_pme))
        
        Entropy_TSsix.append(result[j].TSsix)
        
        
        Enthalpy_old.append(result[j].E_water_old - (result[j].water_num * water_ref_gist))
        
        Water_NUM +=result[j].water_num
    
    worksheet.write(row+2,0,"compound")
    
    worksheet.write(row+2,col,name)
    
    worksheet.write(row+3,0,"Average dH PME-GIST")
    
    
    worksheet.write(row+3,col,sum(Enthalpy)/3)
    
    worksheet.write(row+4,0,"Average TSsix")
    worksheet.write(row+4,col,sum(Entropy_TSsix)/3)
    
    
    worksheet.write(row+5,0,"Average dH GIST-2016")
    
    worksheet.write(row+5,col,sum(Enthalpy_old)/3)
    
    worksheet.write(row+6,0,"Average Water Num")
    worksheet.write(row+6,col,Water_NUM/3)
    
    worksheet.write(row+7,0,"dH PME-GIST sem")
    worksheet.write(row+7,col,stats.sem(Enthalpy))
    
    worksheet.write(row+8,0,"dH GIST-2016 sem")
    worksheet.write(row+8,col,stats.sem(Enthalpy_old))
    
    col+=1

workbook.close()

