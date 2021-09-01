#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:31:15 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# Calculate the system TSsix with the edge voxel removed 

import os 

os.chdir("/Users/eric/Desktop/paper_figure/whole_system_gist")

MD_box_file=open("../32_MD_size.out").readlines()


MD_sizes={}

bulk_entropy=0.0033


for line_index in range(0,len(MD_box_file),3):
    
    #line_index=MD_box_file.index(line)
    
    #max_xyz=[]
    #min_xyz=[]

        
    name=MD_box_file[line_index].split()[1]+"_"+MD_box_file[line_index].split()[-1]
    
    line2=MD_box_file[line_index+1].split()
    #line3=MD_box_file[line_index+2].split()
    
    min_xyz=[10*float(line2[5]),10*float(line2[7]),10*float(line2[9])]
    
    #max_xyz=[10*float(line3[5]),10*float(line3[7]),10*float(line3[9])]
    
    MD_sizes.update({name:min_xyz})
                     
#print(MD_sizes)

MD_sizes["acetamide_MD1"]

from gridData import Grid

import numpy as np


class target:
    
    def __init__(self,name,total_TSsw,total_pop,corrected_TSsw):
        
        self.name=name
        
        self.total_TSsw=total_TSsw
        self.total_pop=total_pop
        #self.region9_pop=region9_pop
        self.corrected_TSsw=corrected_TSsw
        

results=[]

names=sorted(list(MD_sizes.keys()))

for i in names:
    
    print(i)
    
    dat=open(i+"_gist-output.dat").readlines()[2:]
    
    TSsw_noise=0.0
    
    Pop_noise=0.0
    
    
    t=0
    
    for line in dat:
        
        temp=line.split()
        
   
        
        voxel_x = float(temp[1])
        voxel_y = float(temp[2])
        voxel_z = float(temp[3])
        
        """
        
        if voxel_x>MD_sizes[i][0][0] + 0.25  and voxel_x < MD_sizes[i][1][0]-0.25:
            
            if voxel_y>MD_sizes[i][0][1]+0.25 and voxel_y < MD_sizes[i][1][1]-0.25:
                
                if voxel_z>MD_sizes[i][0][2]+0.25 and voxel_z < MD_sizes[i][1][2]-0.25:
                    
                    TSsw+=float(temp[11])
                    
                    Pop=float(temp[4])
                    
        
        """
        
        if (voxel_x<0.5 or voxel_x > MD_sizes[i][0]-0.5
            or voxel_y<0.5 or voxel_y > MD_sizes[i][1]-0.5
            or voxel_z<0.5 or voxel_z > MD_sizes[i][2]-0.5):
            
            #print("haha")
            
            TSsw_noise+=float(temp[11])
            
            Pop_noise+=float(temp[4])
            
            #print(voxel_x,voxel_y,voxel_z)
            
            
            #t=t+1
            

            
            
            
            
            
            
    #region9_pop=np.sum(np.multiply(Grid(i+"_region_9.dx").grid, Grid(i+"_population.dx").grid))
    
    raw_TSsw=np.sum(Grid(i+"_gist-dTSsix-dens.dx").grid)
    
    
    TSsw_t=0.125*(raw_TSsw-TSsw_noise)
    
    Pop_t=np.sum(Grid(i+"_population.dx").grid)-Pop_noise/50000
    
        
    corrected_TSsw=TSsw_t-bulk_entropy*(Pop_t)
    
    print("In efftive region: effetive TSsix: {0} ; effective water number: {1} ; system corrected TSsw {2}".format(TSsw_t,Pop_t,corrected_TSsw))
        
        
    #print(corrected_TSsw)
    
    p=target(i,TSsw_t,Pop_t,corrected_TSsw)
        
    results.append(p)
   

    
"""
print(region9_pop)



print(Pop_t)

print(TSsw_t)

print(raw_TSsw)

TSsw_noise

"""

import xlsxwriter

workbook=xlsxwriter.Workbook("32_mol_system_effective_TSsw_result.xlsx")

worksheet=workbook.add_worksheet()

worksheet.write(0,1,"TSsw in valid region")
worksheet.write(0,2,"water num in valid region")
#worksheet.write(0,3,"water num within 9 of solute")
#worksheet.write(0,3,"bulk-like water number")
worksheet.write(0,3,"corrected system TSsw")

row=1

for r in results:
    
    worksheet.write(row,0,r.name)
    worksheet.write(row,1,r.total_TSsw)
    worksheet.write(row,2,r.total_pop)
    #worksheet.write(row,3,r.region9_pop)
    #worksheet.write(row,4,r.total_pop-r.region9_pop)
    worksheet.write(row,3,r.corrected_TSsw)
    
    row+=1
    
    
    
import scipy  

worksheet.write(100,0,"average corrected  system TSsw")
worksheet.write(101,0,"sem of corrected system TSsw")

col=1

for i in range(0,96,3):
    
    target_name=results[i].name.split("_")[0]
    
    values=[results[i].corrected_TSsw, results[i+1].corrected_TSsw, results[i+2].corrected_TSsw]
    
    mean_corrected_TSsw=sum(values)/3
    
    sem=scipy.stats.sem(values)
    
    worksheet.write(99,col,target_name)
    worksheet.write(100,col,mean_corrected_TSsw)
    worksheet.write(101,col,sem)
    
    col+=1
    
workbook.close()
    
    
    
    
    

       
        
        
        

                    
                    
                    
                    
                    
                    
                    
        
        
        
   
        
        
    
    