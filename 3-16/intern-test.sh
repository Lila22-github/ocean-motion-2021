#!/bin/bash

cd ../2-25

 STRING="START"
 echo $STRING

#compiling files   
 gfortran -O3 -o vectorq.exe vectorq.f
 gfortran -O3 -o omegainv.exe omegainv.f

while read p; do
  #creating exec files with all dates
  python writing_to_file_omegainv.py $p
  python Writing_to_file_vectorq.py $p

  #running exec files
  ./vectorq.exec
  ./omegainv.exec
  echo $p
done <date_list.txt

 STRING="DONE"
 echo $STRING

# in date forloop include writing to file scripts 
# take the resulting omegainv and vectorq and run with the 4 terminal commands
