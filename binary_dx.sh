#!bin/bash

# for every ligand, generate a series of binary dx file, in which the voxel value is 1 when the voxel is within certern distant to the heavey atom of the ligand
distances=(1 1.25 1.5 1.75 2 2.25 2.5 2.75 3 3.25 3.5 3.75 4 4.25 4.5 4.75 5 5.25 5.5 5.75 6 6.25 6.5 6.75 7 7.25 7.5 7.75 8 8.25 8.5 8.75 9 9.25 9.5 9.75 10 10.25 10.5 10.75 11 11.25 11.5 11.75 12 12.25 12.5 12.75 13 13.25 13.5 13.75 14 14.25 14.5 14.75 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30)
for d in ${distances[@]}
do
	for ligand in *prod.pdb
		do


			gistpp -i ${ligand%%prod*}population.dx -i2 $ligand -op defbp -opt const $d -o ${ligand%%prod*}region_${d}.dx
			echo "$ligand done"
		done
done