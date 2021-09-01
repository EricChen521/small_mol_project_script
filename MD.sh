#!/bin/bash                                                              

SANDER="pmemd.cuda -AllowSmallBox"

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


$SANDER -i min.in -p pure_water.prmtop -c pure_water.rst7 -ref pure_water.rst7 -O -o min_sol.out -e min_sol.en -inf min_sol.info -r min_sol.rst7 -l min_sol.log
$SANDER -i heat.in -p pure_water.prmtop -c min_sol.rst7 -ref min_sol.rst7 -O -o heat_sol.out -e heat_sol.en -inf heat_sol.info -r heat_sol.rst7 -x heat_sol.nc -l heat_sol.log
$SANDER -i press.in -p pure_water.prmtop -c heat_sol.rst7 -ref heat_sol.rst7 -O -o press_sol.out -e press_sol.en -inf press_sol.info -r press_sol.rst7 -x press_sol.nc -l press_sol.log
$SANDER -i eq_MD.in -c press_sol.rst7 -ref press_sol.rst7 -p pure_water.prmtop -O -o eq.out -inf eq.info -e eq.en -r eq.rst7 -x eq.nc -l eq.log
$SANDER -i NPT_prod.in -c eq.rst7 -ref eq.rst7 -p pure_water.prmtop -O -o prod.out -inf prod.info -e prod.en -r prod.rst7 -x prod.nc -l prod.log

