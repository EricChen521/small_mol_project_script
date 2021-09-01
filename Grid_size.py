# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:18:20 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


# adjust GRID box size to see the convergence, for benzene the farest hydorgen
#distance is about 5.03 A

import os 


from gridData import Grid
 
import numpy as np

import matplotlib.pyplot as plt

os.chdir("/Users/eric/Desktop/paper_figure/solvation_free_energy/benz_converge")

#file1 for entropy
#file1=open("benz_full_energy.dat").readlines[2:]

#file2 
#file2=open("benz_half_energy.dat").readlines[2:]

file1=Grid("gist-dTSsix-dens.dx").grid

file2=Grid("gist-Etot-pme-dens.dx").grid

file3=Grid("gist-gO.dx").grid

file4=Grid("gist-neighbor-norm.dx").grid


coordinates=Grid("gist-gO.dx").edges











entropy=[]

energy=[]





water_num=[]

for i in range(31):
    
    temp1=0.125 * np.sum(file1[30-i:30+i,30-i:30+i,30-i:30+i])
    
    temp2=0.125 * np.sum(file2[30-i:30+i,30-i:30+i,30-i:30+i])
    
    temp3=0.03288 * 0.125* np.sum(file3[30-i:30+i,30-i:30+i,30-i:30+i])
    
    
    
    entropy.append(temp1)
    energy.append(temp2)
    water_num.append(temp3)
    

x=[i for i in range(31)]

dE=[energy[i] - (-9.542238)*water_num[i] -8.10 for i in range(31)]

min(entropy)

min(energy)

entropy.index(min(entropy))

entropy[-1] - min(entropy)

noise_water_num=water_num[-1] - water_num[13]

water_num[13]

water_num[-1]

# in bulk water 882.691340 water has dTSsix 2.125585 Kcal/mol

# here we have 815.24 water, 2.586 


entropy[-1]

print(dE)

max(water_num)

dE[13]

plt.plot(x, entropy, color="orange",label="TSsix")
plt.plot(x,dE,color="blue",label="Delta H")
plt.xlabel("Grid size in Å ")
plt.ylabel("Kcal/mol")
plt.legend()
plt.savefig("Benz_converge.png",dpi=400)
plt.show()

print(x)
print(entropy)
print(dE)

# [17,43] includes the most parts of the signal

np.any(file4[:,0] == 5.25)

S_total=0

W_total=0

Neighbor_list=[]

X=[] # signal first order ent
Y=[]


for i in range(17,43):
    
    for j in range(17,43):
        
        for k in range(17,43):
            
            raw=file1[i,j,k]
            
           # print(file4[i,j,k])
           
            neigh=file4[i,j,k]
            
            Neighbor_list.append(neigh)
            
            
            water_count=file3[i,j,k] * 0.03288 * 0.125
            
            
            
            
           
            W_total += water_count 
            
            S_total += 0.125 * raw
            
            
            """
           
            if neigh < 5.25:
               
                total = 0.125 * raw + (neigh/5.25)*water_count*3.471
               
            if neigh >= 5.25:
               
                total = 0.125 * raw + water_count * 3.571
        
            
            #total=0.125 * (1+file4[i,j,k]/(5.25000001-file4[i,j,k])) * raw
            
            
            
            S_total += total
            
            """




print(W_total)

print(S_total)

nei_mean=sum(Neighbor_list)/len(Neighbor_list)

print(sum(Neighbor_list)/len(Neighbor_list))



dS = S_total + nei_mean/5.25 * 3.471 * W_total - W_total * 3.471

print(dS)



plt.scatter(X,Y,s=10)
plt.xlabel("Voxel TSsix in Kcal/mol") 
plt.ylabel("Normalized water neighbor")
plt.show()
            
plt.hist(file4[17:43,17:43,17:43].ravel(),bins=50)


np.max(file4[17:43,17:43,17:43])

np.mean(file4[17:43,17:43,17:43])

np.sum(file1[17:43,17:43,17:43])

plt.xlabel("water neighbor # within first shell")

plt.ylabel("Counts")   

plt.legend()

plt.show()


out_file=Grid(file4[17:43,17:43,17:43],edges=[coordinates[0][17:43],coordinates[1][17:43],coordinates[2][17:43]]).export("signal.dx","DX")
    
    





