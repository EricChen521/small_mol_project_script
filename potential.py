# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 08:12:37 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


# find out whether the potential energy in TI incude the ligand energy

import os

os.chdir("D:/eric/Entropy_esti/TI_potential/6LU7")

file1=open("ligand_energy.out").readlines()

file2=open("system_energy.out").readlines()

file3=open("ti001.en").readlines()

ligand_vdw=[]

ligand_elec=[]

sys_vdw=[]
sys_elec=[]

ti_vdw=[]
ti_elec=[]


for line in file1[1:]:
    
    v=float(line.split()[6])
    e=float(line.split()[7])
    
    ligand_vdw.append(v)
    ligand_elec.append(e)
    
for line in file2[1:]:
    
    v=float(line.split()[6])
    e=float(line.split()[7])
    sys_vdw.append(v)
    sys_elec.append(e)
    
for line in file3[26:]:
    
    if "L6" in line:
        
        v=float(line.split()[3])
        
        e=float(line.split()[4])
        
        ti_vdw.append(v)
        ti_elec.append(e)
        
        
# The vdw

MD_remain_vdw=[sys_vdw[i]-ligand_vdw[i] for i in range(9)]

MD_remain_elec=[sys_elec[i] -ligand_elec[i] for i in range(9)]  


diff_vdw=[MD_remain_vdw[i] - ti_vdw[i] for i in range(9)]

diff_elec=[MD_remain_elec[i] - ti_elec[i] for i in range(9)]


#print(diff_vdw)

#print(diff_elec)

ti_elec_average=sum(ti_elec[0:9])/9

ti_vdw_average=sum(ti_vdw[0:9])/9

sys_elec_average=sum(sys_elec[0:9])/9

sys_vdw_average=sum(sys_vdw[0:9])/9

ligand_elec_average=sum(ligand_elec[0:9])/9

ligand_vdw_average=sum(ligand_vdw[0:9])/9

print("sys_vdw: {0}, ligand_vdw: {1}, ti_vdw: {2}".format(sys_vdw_average,ligand_vdw_average,ti_vdw_average))
    
print("sys_elec: {0}, ligand_vdw: {1}, ti_elec: {2}".format(sys_elec_average,ligand_elec_average,ti_elec_average))    
    
    


import matplotlib.pyplot as plt
import numpy as np

x=np.array([270,270,270,270,270,280,280,280,280,280,300,300,300,300,300,320,320,320,320,320,330,330,330,330,330])


y=np.array([-3.99564,-3.91414,-3.86795,-4.00976,-4.02764,-3.61108,-3.9607,-3.71852,-3.74738,-3.87492,-3.32556,-3.33691,-3.43394,-3.47257,-3.19114,-3.11318,-3.11668,-3.02375,-3.01466,-2.90144,-3.14437,-3.00234,-2.88138,-2.83993,-3.02151])

m,b = np.polyfit(x,y,1)

#plt.plot(x,y,"o")
plt.scatter(x,y)
plt.plot(x,m*x+b,color="red")

print(m,b)

from scipy import stats

slope, intercept,r_value,p_value,std_error  = stats.linregress(x,y)

print("slope:",slope)

 print("intercept:", intercept)

print("r_value:",r_value)

print("std_error:", std_error)

# for all points slope
import math

SE_slope= 30 * math.sqrt(25/(26*23)) * std_error 

Y=[slope * i + intercept for i in x]

Y_d2= [ (Y[i] - y[i])**2 for i in range(len(Y)) ]

X_d2= [ (x[i] - 300)**2 for i in range(len(x))]


se_slope = math.sqrt(sum(Y_d2)/((len(x)-2)*sum(X_d2)))




print("all points slope se: ", SE_slope)

print("se all points slope se_slope: ", se_slope)

300* se_slope
