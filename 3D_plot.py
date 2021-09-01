# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:26:09 2020

@author: Eric Chen, The Graduate Center, City University of new york 

@email: eric.clyang@gmail.com
"""


from mpl_toolkits.mplot3d import Axes3D

from mpl_toolkits.mplot3d.axes3d import get_test_data

from gridData import Grid


%matplotlib notebook

import numpy as np

import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

x=y=z=np.arange(0,60,1)

#values=Grid("gist-Etot-pme-dens.dx").grid

#values=Grid("gist-dA.dx").grid

#plt.hist(list(values.flatten()),bins=50)

#np.count_nonzero(values==0)

pme_norm=np.zeros((60,60,60))

file=open("gist-output.dat").readlines()[2:]

for i in range(60):
    
    for j in range(60):
        
        for k in range(60):
            
            num= 3600*i + 60*j +k
            pme_norm[i,j,k]=float(file[num].split()[18])
            
pme_norm[0,0,0]       

#np.max(values)
#np.min(values)

data=[]

for x in range(15,45):
    
    for y in range(15,45):
        
        for z in range(15,45):
            
            if pme_norm[x,y,z] <= 0:
                
            
                c=[x,y,z,pme_norm[x,y,z]]
                data.append(c)
            
data=np.array(data)          

cm=plt.cm.get_cmap("bwr")
sp=ax.scatter(data[:,0],data[:,1],data[:,2],s=0.1,c=data[:,3])

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.colorbar(sp)


            
    

