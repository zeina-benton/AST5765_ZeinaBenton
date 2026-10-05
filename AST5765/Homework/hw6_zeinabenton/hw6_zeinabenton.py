#Zeina Benton
#Homework 6
#10/5/26

#%%
import os

print("Problem 2")
#a
#Retrieve practicum 4 information:
datadir = "/Users/zeinabenton/Desktop/AST5765/AST5765_ZeinaBenton/AST5765_ZeinaBenton-1/AST5765/Handin/Practicum4_zeinabenton/hw6_data/" #This is the path to the data directory
fext = ".fits" #This is the file extension of the data files
objprefix = "rdpharocor_stars_13s_" #Prefix for the object images for fits compliant
darkprefix = "rdpharocor_dark_13s_" #Prefix for the dark images for fits compliant

objfile = []
darkfile = []

for filename in sorted(os.listdir(datadir)): #in case the files are not in order
        root = filename[:-len(fext)]

        if filename.startswith(objprefix):
            objfile.append(root)

        elif filename.startswith(darkprefix):
            darkfile.append(root)

#Now begin hw6 new code:
from hw6_zeinabenton_supportfunctions import 

