# PTRAC_POS2CSV
These instructions should be followed to plot the SDEF source point created by MCNP and exported by means of the PTRACT fuction (based on MCNP5.1.6 release).
This routine only converts the PTRAC file into a csv file which can be later loaded in Paraview.

## How to use the routine
    > python PTRAC_POS2CSV.py -i PTRAC_filename -o CSV_outputfilename

## Complete instructions
1) Run MCNP with the following instruction or similar
    
        > PTRAC NPS=1,1e7 TYPE=P WRITE=pos FILE=asc EVENT=src MAX=1e5
    
2) Run the Python3.6 PTRAC_POS2CSV.py routine.
   
        > PTRAC_POS2CSV.py -i PTRAC_filename -o CSV_outputfilename
 
3) Load the csv text file in Paraview.
 
4) Use the filter "Table to Point" selecting the right variables for X, Y and Z. 
Remember to tick the "Mantain all variable" to be able to visualize also the ""scalar" field.
    
5) Plot the "Table to Point" in a 3D render

6) Enjoy ... =)


## LICENSE
Copyright 2019 F4E | European Joint Undertaking for ITER and the Development of Fusion Energy (‘Fusion for Energy’). Licensed under the EUPL, Version 1.1 or - as soon they will be approved by the European Commission - subsequent versions of the EUPL (the “Licence”). You may not use this work except in compliance with the Licence. You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl.html   
Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an “AS IS” basis, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the Licence permissions and limitations under the Licence.