#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:38:21 2020

@author: Eric Chen, Graduate Center, City University of New York

@contact: eric.clyang521@gmail.com
"""

# calculate the radium where the energy and entropy are converged 

import os

#os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/PME-GIST")

os.chdir("/Users/eric/Desktop/paper_figure/whole_system_gist")

import glob

import numpy as np

import matplotlib.pyplot as plt

from gridData import Grid

PME_water_ref=-9.5422

GIST_water_ref=-9.5352

bulk_entropy=0.0033

ligand_files=sorted(glob.glob("*prod.pdb"))

#distances=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]

distances=["1","1.25","1.5","1.75","2","2.25","2.5","2.75","3","3.25","3.5","3.75"
           ,"4","4.25","4.5","4.75","5","5.25","5.5","5.75","6","6.25","6.5","6.75","7"
           ,"7.25","7.5","7.75","8","8.25","8.5","8.75","9","9.25","9.5","9.75",
           "10","10.25","10.5","10.75","11","11.25","11.5","11.75","12",
           "12.25","12.5","12.75","13","13.25","13.5","13.75","14","14.25","14.5","14.75","15"]

"""

distances=["1","1.25","1.5","1.75","2","2.25","2.5","2.75","3","3.25","3.5","3.75"
           ,"4","4.25","4.5","4.75","5","5.25","5.5","5.75","6","6.25","6.5","6.75","7"
           ,"7.25","7.5","7.75","8","8.25","8.5","8.75","9","9.25","9.5","9.75",
           "10","10.25","10.5","10.75","11","11.25","11.5","11.75","12",
           "12.25","12.5","12.75","13","13.25","13.5","13.75","14","14.25","14.5","14.75","15","16","17","18","19"
           ,"20","21","22","23","24","25","26","27","28","29","30"]

"""
#regions=sorted(glob.glob("lig_MD3*region*dx"))

len(distances)



# plot out the converge line for 32 mols

ligand_self={}
ligand_pme={}



file1=open("32_mols_ligand_self.energy").readlines()

for i in range(3,128,4):
    
    name=file1[i].strip()
    v1=float(file1[i-3])
    v2=float(file1[i-2])
    v3=float(file1[i-1])
    
    v_mean=(v1+v2+v3)/3
    ligand_self.update({name:v_mean})
    
    
file2=open("32_mols_solute_half_pme.energy").readlines()

for i in range(3,128,4):
    
    name=file2[i].strip()
    v1=float(file2[i-3])
    v2=float(file2[i-2])
    v3=float(file2[i-1])
    v_mean=(v1+v2+v3)/3
    ligand_pme.update({name:v_mean})
    
    
#ligand_self["simazine"]

#fonts=100

#ticks=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

for lig in sorted(list(ligand_self.keys()))[1:]:
    
    print("Make converge PNG for ligand:{}".format(lig))
    
    corrected_TSsix=[]

    PME_Energy=[]
    
    GIST_Energy=[]

    Pop=[]

    
    for d in distances:
        print(d)
    
    
    
    # energy
    
        PME_E_dens=np.multiply(Grid(lig+"_MD3_gist-Etot-pme-dens.dx").grid,Grid(lig+"_MD3_region_"+d+".dx").grid)
        
        #GIST_Eww_dens=np.multiply(Grid(lig+"_MD3_gist-Eww-dens.dx").grid,Grid(lig+"_MD3_region_"+d+".dx").grid)
        
        #GIST_Esw_dens=np.multiply(Grid(lig+"_MD3_gist-Esw-dens.dx").grid,Grid(lig+"_MD3_region_"+d+".dx").grid)
        
        #GIST_E_dens=np.add(0.5*GIST_Esw_dens,GIST_Eww_dens)
    

    
        pop = np.multiply(Grid(lig+"_MD3_population.dx").grid,Grid(lig+"_MD3_region_"+d+".dx").grid)
    
    
    
        TSsix_dens=np.multiply(Grid(lig+"_MD3_gist-dTSsix-dens.dx").grid,Grid(lig+"_MD3_region_"+d+".dx").grid)
    
   
    
        PME_Energy.append(np.sum(PME_E_dens)*0.125+ligand_pme[lig]-ligand_self[lig]-PME_water_ref*np.sum(pop))
        #PME_Energy.append(np.sum(PME_E_dens)*0.125-PME_water_ref*np.sum(pop))
        
        #GIST_Energy.append(np.sum(GIST_E_dens)*0.125-GIST_water_ref*np.sum(pop))
        
        corrected_TSsix.append(np.sum(TSsix_dens)*0.125-0.0033*np.sum(pop))
    
        Pop.append(np.sum(pop))
    
    


    
    radius=[i for i in distances]
    
    # remove the bulk water systematic error
    
    #signal_entropy=min(TSsix)
    
    #signal_index=TSsix.index(signal_entropy)
    
    #signal_index=32 # cut from 9 A
    
    #signal_pop=Pop[signal_index]
    
    #pop_bulk=[Pop[i]-signal_pop for i in range(signal_index+1,len(Pop))]
    
    
    #corrected_TSsix=TSsix[:signal_index+1]+[TSsix[signal_index+1+t] - bulk_entropy*pop_bulk[t] for t in range(len(pop_bulk)) ]



    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    
    ax.plot(radius, corrected_TSsix, color="orange",label="T\u0394"+"$S_{sw}$")
    #ax.plot(radius,TSsix,color="green",label="TSsix")
    ax.plot(radius,PME_Energy,color="blue",label="\u0394"+"$E_{solv}$")
    #ax.plot(radius,GIST_Energy,color="red",label="GIST-2016")

    ax.set_xlabel("Integrating distance from solute in Å ")
    ax.set_ylabel("Kcal/mol")
    
    #plt.xlim(1,30)
    plt.xticks(np.arange(0,60,4),rotation="vertical")
    plt.legend()
    plt.tight_layout()
    plt.savefig(lig+"_converge.png",dpi=400)
    plt.show()

## Entropy Correlation##

"""
X=[i for i in range(10)]

Y=[2*i for i in X ]

Z= [3*i for i in X]

plt.plot(X,Y,color="orange",label="T\u0394"+"$S_{sw}$")
plt.plot(X,Z,color="red",label="\u0394"+"$E_{solv}$")
plt.legend()

plt.show()

"""

### get the TI entropy from xlsx file

import xlrd

file=xlrd.open_workbook("../solvation_free_energy/data_summary.xlsx")

sheet=file.sheet_by_index(0)

import xlsxwriter

workbook=xlsxwriter.Workbook("radius_converge_result.xlsx")
worksheet=workbook.add_worksheet()
worksheet.write(0,0,"Radius from heavey atom")
worksheet.write(0,1,"dH_PME_slope")
worksheet.write(0,2,"dH_PME_intercept")
worksheet.write(0,3,"dH_PME_R_square")

worksheet.write(0,4,"dH_GIST_slope")
worksheet.write(0,5,"dH_GIST_intercept")
worksheet.write(0,6,"dH_GIST_R_square")


worksheet.write(0,7,"S_slope")
worksheet.write(0,8,"S_intercept")
worksheet.write(0,9,"S_R_square")

worksheet.write(0,10,"dG_PME_slope")
worksheet.write(0,11,"dG_PME_intecept")
worksheet.write(0,12,"dG_PME_R_square")

worksheet.write(0,13,"dG_PME abs mean diff")
TI_entropy=[]
TI_enthalpy=[]
TI_G=[]




for row in range(1,33):
    
    name=sheet.cell_value(row,0)
    
    value_H=sheet.cell_value(row,1)
    value_S=sheet.cell_value(row,2)
    value_G= value_H - value_S
    
    
    TI_enthalpy.append(value_H)
    TI_entropy.append(value_S)
    
    TI_G.append(value_G)
    



from scipy import stats 

row=1

#for d in ["8"]:
  
#from sklearn.metrics import mean_squared_error


# The correlation using difference radium distance
Radius=["9","10","11","12","13","14","15"]

POP=[0]



#Radius=["4"]


workbook2=xlsxwriter.Workbook("radius_local_values.xlsx")
worksheet2=workbook2.add_worksheet()

worksheet2.write(0,0,"ligand")

COL=1

for d in Radius:
    
    worksheet2.write(0,COL,"dH_PME_radius_"+d)
    worksheet2.write(0,COL+1,"dH_GIST_radius_"+d)
    worksheet2.write(0,COL+2,"dTSsw_radius_"+d)
    worksheet2.write(0,COL+3,"water_num_within_radius_"+d)
    
    COL+=4


COL=0

for d in Radius:
    
    
        
    print("local region of {0}".format(d))
    
    PME_enthalpy=[]
    
    GIST_enthalpy=[]
    GIST_entropy=[]
    GIST_G=[]
    
    ROW=1
        
    for lig in sorted(list(ligand_self.keys())):
        
        
        
        
        print(lig)
        
        PME_E_dens=0
        GIST_Eww_dens=0
        GIST_Esw_dens=0
        pop=0
        TSsix_dens=0
        
        
        
        
        
    
    
    
        for MD in ["MD1","MD2","MD3"]:
            
    
            PME_E_dens += np.sum(np.multiply(Grid(lig+"_"+MD+"_gist-Etot-pme-dens.dx").grid,Grid(lig+"_"+MD+"_region_"+d+".dx").grid))
            
            GIST_Eww_dens += np.sum(np.multiply(Grid(lig+"_"+MD+"_gist-Eww-dens.dx").grid,Grid(lig+"_"+MD+"_region_"+d+".dx").grid))
    
            GIST_Esw_dens += np.sum(np.multiply(Grid(lig+"_"+MD+"_gist-Esw-dens.dx").grid,Grid(lig+"_"+MD+"_region_"+d+".dx").grid))
    
            pop += np.sum(np.multiply(Grid(lig+"_"+MD+"_population.dx").grid,Grid(lig+"_"+MD+"_region_"+d+".dx").grid))
    
    
    
            TSsix_dens += np.sum(np.multiply(Grid(lig+"_"+MD+"_gist-dTSsix-dens.dx").grid,Grid(lig+"_"+MD+"_region_"+d+".dx").grid))
    
   
        PME_enthalpy.append((PME_E_dens/3)*0.125+ligand_pme[lig]-ligand_self[lig]-PME_water_ref*(pop/3))
        
        
        GIST_enthalpy.append((0.125*(GIST_Eww_dens+GIST_Esw_dens)/3)-GIST_water_ref*(pop/3))
        
        POP.append(pop/3)
        
        raw_TSsix=(TSsix_dens/3)*0.125
        
        bulk_entropy_noise=(POP[-1]-POP[-2])*bulk_entropy
        
        corrected_TSsix=raw_TSsix-bulk_entropy_noise
        
        
        GIST_entropy.append(corrected_TSsix)
        #GIST_G.append(GIST_enthalpy[-1]-GIST_entropy[-1])
        
        #print("water num in this radius: {}".format(pop/3))
        
        
        
        worksheet2.write(ROW,0,lig)
        
        
        
        worksheet2.write(ROW,4*COL+1,PME_enthalpy[-1])
        
        worksheet2.write(ROW,4*COL+2,GIST_enthalpy[-1])
        
        worksheet2.write(ROW,4*COL+3,GIST_entropy[-1])
        worksheet2.write(ROW,4*COL+4,pop/3)
        
        ROW+=1
        
        
    COL+=1
        
    """   
        
    # calculate the correlation
    
    print("TI_enthalpy:")
    print(TI_enthalpy)
    
    print("GIST_enthalpy:")
    print(GIST_enthalpy)
    
    print("TI_entropy:")
    print(TI_entropy)
    
    print("GIST_entropy")
    print(GIST_entropy)
    
    """
    
    
    
    H_slope, H_intercept,H_r_value,H_p_value,H_std_error  = stats.linregress(TI_enthalpy,PME_enthalpy)
    
    h_slope,h_intercept,h_r_value,h_p_value,h_std_error = stats.linregress(TI_enthalpy,GIST_enthalpy)
    
    S_slope, S_intercept,S_r_value,S_p_value,S_std_error  = stats.linregress(GIST_entropy,TI_entropy)
    
    GIST_fitted_S=[(S_slope*s+S_intercept) for s in GIST_entropy]
    
    GIST_fitted_dG=[GIST_enthalpy[i] - GIST_fitted_S[i] for i in range(len(GIST_enthalpy))]
    
    """
    
    print("TI dG:")
    print(TI_G)
    
    print("PME_GIST fitted dG:")
    print(GIST_fitted_dG)
    
   """
        
        
        
        
    G_slope, G_intercept,G_r_value,G_p_value,G_std_error  = stats.linregress(TI_G,GIST_fitted_dG)
    
    abs_diff=[TI_G[t]-GIST_fitted_dG[t] for t in range(len(TI_G))]
    
    mean_abs_diff=sum(abs_diff)/len(abs_diff)
    
    
    
    #print("PME Enthalpy slope:{0}, intercept:{1}, R2:{2}".format(H_slope,H_intercept,H_r_value**2))
    
    #print("GIST Enthalpy slope:{0}, intercept:{1}, R2:{2}".format(h_slope,h_intercept,h_r_value**2))
    
    print("Entropy slope:{0}, intecept:{1}, R2:{2}".format(S_slope,S_intercept,S_r_value**2))
    
    #print("delta_G slope:{0}, intecept:{1}, R2:{2}".format(G_slope,G_intercept,G_r_value**2))
    
    
    worksheet.write(row,0,d)
    
    worksheet.write(row,1,H_slope)
    worksheet.write(row,2,H_intercept)
    worksheet.write(row,3,H_r_value**2)
    
    worksheet.write(row,4,h_slope)
    worksheet.write(row,5,h_intercept)
    worksheet.write(row,6,h_r_value**2)
    
    
    
    worksheet.write(row,7,S_slope)
    worksheet.write(row,8,S_intercept)
    worksheet.write(row,9,S_r_value**2)
    
    worksheet.write(row,10,G_slope)
    worksheet.write(row,11,G_intercept)
    worksheet.write(row,12,G_r_value**2)
    worksheet.write(row,13,mean_abs_diff)
    
    row+=1
    
    
    
    
workbook.close()  

workbook2.close()
    
    
    
  
print(TI_enthalpy)
print(GIST_enthalpy)

print(TI_entropy)
print(GIST_entropy)

print(S_slope)
print(S_intercept)

print(GIST_fitted_S)
            
        
        

print(sorted(ligand_self.keys()))


    
    