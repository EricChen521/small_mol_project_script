# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:16:33 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


import os

os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/TI")

file1=open("270K_ti_32mols.result").readlines()
file2=open("300K_ti_32mols.result").readlines()
file3=open("330K_ti_32mols.result").readlines()

import numpy as np

temp=np.array([270,270,270,300,300,300,330,330,330])
mols=[]

for i in range(9,320,10):
    
    mols.append(file1[i].split()[0])
    
G_270=[]
G_300=[]
G_330=[]

for line in file1:
    
    if "." in line.split()[0]:
        
        G_270.append(float(line.split()[0]))
        
for line in file2:
    
    if "." in line.split()[0]:
        G_300.append(float(line.split()[0]))
        

for line in file3:
    
    if "." in line.split()[0]:
        
        G_330.append(float(line.split()[0]))
        

mol_G={}

import xlsxwriter

workbook=xlsxwriter.Workbook("32mol_ti_result.xlsx")
worksheet=workbook.add_worksheet()


row=1

for i in range(32):
    
    key=mols[i]
    values=G_270[3*i:3*i+3] + G_300[3*i:3*i+3] + G_330[3*i:3*i+3]
    
    
    mol_G.update({key:values})
    
#print(mol_G["acetamide"])  

# calculate the slope and standard error of the slope


from scipy import stats

import math

for i in mols:
    
    col=0
    
    #print("Molecule: %s".format(i))
    
    y=mol_G[i]
    
    
    #print(y)
    worksheet.write(row,col,i)
    
    col=col+1
    
    for j in y:
        
        worksheet.write(row,col,j)
        col=col+1
    
    slope, intercept,r_value,p_value,std_error  = stats.linregress(temp,y)
    
    y_predicted=[slope * i + intercept for i in temp]
    
    y2= [ (y_predicted[i] - y[i])**2 for i in range(len(y)) ]
    
    x2= [ (temp[i] - 300)**2 for i in range(len(temp))]
    
    slope_se=math.sqrt(sum(y2)/[(len(temp)-2)*sum(x2)])
    
    worksheet.write(row,col,-300*slope)
    worksheet.write(row,col+1,300*slope_se)
    worksheet.write(row,col+2,r_value**2)
    
    dG_300K=sum(y[3:6])/3
    
    dH_300K=dG_300K + (-300*slope)
    
    worksheet.write(row,col+3,dH_300K)
    worksheet.write(row, col+4,dG_300K)
    
    row=row+1
    
    
    print("Molecule: {0}; TS: {1}; standard mean error: {2}; R2: {3}\n".format(i, -300*slope,300*slope_se,r_value**2))

workbook.close()