'''
########################################################################################################
# Copyright 2019 F4E | European Joint Undertaking for ITER and the Development                         #
# of Fusion Energy (‘Fusion for Energy’). Licensed under the EUPL, Version 1.1                         #
# or - as soon they will be approved by the European Commission - subsequent versions                  #
# of the EUPL (the “Licence”). You may not use this work except in compliance                          #
# with the Licence. You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl.html       #
# Unless required by applicable law or agreed to in writing, software distributed                      #
# under the Licence is distributed on an “AS IS” basis, WITHOUT WARRANTIES                             #
# OR CONDITIONS OF ANY KIND, either express or implied. See the Licence permissions                    #
# and limitations under the Licence.                                                                   #
########################################################################################################
'''

# Author: Marco Fabbri
# Date  : 2019/07/17 16:00
# 
# These instructions should be followed to plot the SDEF source point created by
# MCNP and exported by means of the PTRACT fuction (based on MCNP5.1.6 release).
# This routine only converts the PTRAC file into a csv file which can be later loaded
# in Paraview.
# 
# 1) Run MCNP with the following instruction or similar
#    "PTRAC NPS=1,1e7 TYPE=P WRITE=pos FILE=asc EVENT=src MAX=1e5"
#    
# 2) Run the Python3.6 PTRAC_POS2CSV.py routine.
#    PTRAC_POS2CSV.py -i PTRAC_filename -o CSV_outputfilename
# 
# 3) Load the csv text file in Paraview.
# 
# 4) Use the filter "Table to Point" selecting the right variables for X, Y and Z.
#    Remember to tick the "Mantain all variable" to be able to visualize also the
#    "scalar" field.
#    
# 5) Plot the "Table to Point" in a 3D render
# 
# 6) Enjoy ... =)


import numpy as np

import argparse
parser = argparse.ArgumentParser(description='Routine which analyses a PTRAC output creating a csv file with the source point computed. This can be later loaded in the Paraview for the proper visualization.')
parser.add_argument('-i',help='insert input PTRAC filename',
                    type=str,
                    default='')
parser.add_argument('-o',help='insert output CSV filename',
                    type=str,
                    default='')
parser.add_argument('-version',action='version',
                   version='<< PTRAC2POSCSV v1.2 >>')

args = parser.parse_args()

# inputFILE  = 'ptrac'
# outputFILE = 'POINT_2_PARAVIEW.csv'

with open(args.o,"w") as outfile:
    outfile.write("Points:0, "+"Points:1, "+"Points:2, "+"scalars"+'\n')
    with open(args.i,"r") as infile:
        Flag = False
        for line in infile:
            split=line.split()
            if Flag == False:   # Flag to jump to the PTRAC MCNP data output
                if np.size(split) == 2: 
                    Flag =True
            if Flag == True:
                if np.size(split) == 3:
                    outfile.write(split[0]+", "+split[1]+", "+split[2]+", 1"+'\n')
                