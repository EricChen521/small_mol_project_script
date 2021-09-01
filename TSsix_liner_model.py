#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:43:31 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# estimated the TdS by TSsix by liner model

import os

#os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy")

os.chdir("/Users/eric/Desktop/paper_figure/")


import xlrd

import random

#file=xlrd.open_workbook("data_summary.xlsx")

file=xlrd.open_workbook("Whole_size_summary.xlsx")
sheet=file.sheet_by_index(0)

class molecule:
    def __init__(self,name,TdS,TSsix):
        
        self.name=name
        self.TdS=TdS
        self.TSsix=TSsix

mols=[]

for row in range(1,33):
    
    name=sheet.cell_value(row,0)
    TdS=float(sheet.cell_value(row,2))
    TSsix=float(sheet.cell_value(row,16))
    mols.append(molecule(name,TdS,TSsix))
 
"""  
mols[1].name
mols[1].TSsix
mols[1].TdS
"""

from scipy import stats 

slopes=[]

intercepts=[]

R2=[]

RMSE=[]

from sklearn.metrics import mean_squared_error

N=1000

for i in range(N):
    
    random.shuffle(mols)
    training=mols[0:24]
    testing=mols[24:]
    
    train_TdS=[mol.TdS for mol in training]
    train_TSsix=[mol.TSsix for mol in training]
    
    slope, intercept,r_value,p_value,std_error  = stats.linregress(train_TSsix,train_TdS)
    
    slopes.append(slope)
    intercepts.append(intercept)
    R2.append(r_value**2)
    
    Test_TSsix=[mol.TSsix for mol in testing]
    
    predicted_TdS=[float(slope*j+intercept) for j in Test_TSsix]
    
    true_TdS=[mol.TdS for mol in testing]
    
    rmse=mean_squared_error(true_TdS, predicted_TdS)
    
    RMSE.append(rmse)
    
    
    
print(slopes)  

import matplotlib.pyplot as plt

plt.hist(slopes,bins=40)
plt.show()

print(intercepts)

print(R2)

print(RMSE)
    
sum(RMSE)/len(RMSE)

import xlsxwriter

workbook=xlsxwriter.Workbook("liner_model.xlsx")
worksheet=workbook.add_worksheet()

worksheet.write(0,1,"slope")
worksheet.write(0,2,"intercept")
worksheet.write(0,3,"R2")
worksheet.write(0,4,"RMSE")

row=1

for i in range(N):
    
    worksheet.write(row,0,"shuffle_"+str(i))
    worksheet.write(row,1,slopes[i])
    worksheet.write(row,2,intercepts[i])
    worksheet.write(row,3,R2[i])
    worksheet.write(row,4,RMSE[i])
    row+=1

workbook.close()
    

whole_TSsix=[mol.TSsix for mol in mols]

whole_TdS=[mol.TdS for mol in mols]

slope, intercept,r_value,p_value,std_error  = stats.linregress(whole_TSsix,whole_TdS)

Y_predicted=[float(slope*i+intercept) for i in whole_TSsix]

whole_RMSE=mean_squared_error(whole_TdS,Y_predicted )

print(whole_RMSE)



