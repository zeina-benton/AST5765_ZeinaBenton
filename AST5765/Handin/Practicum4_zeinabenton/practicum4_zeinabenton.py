#Zeina Benton
#Practicum 4
#10/1/26

#%%
print("Problem 2")
#a
import os
datadir = "hw6_data/" #This is the path to the data directory
fext = ".fits" #This is the file extension of the data files

objprefix = "rdpharocor_stars_13s_" #Prefix for the object images for fits compliant
darkprefix = "rdpharocor_dark_13s_" #Prefix for the dark images for fits compliant

#B
objfile = []
darkfile = []

for filename in sorted(os.listdir(datadir)): #in case the files are not in order
        root = filename[:-len(fext)]

        if filename.startswith(objprefix):
            objfile.append(root)

        elif filename.startswith(darkprefix):
            darkfile.append(root)

#c
print("Data directory:", datadir)
print("FITS extension:", fext)
print("Last target filename:", objfile[-1]) #Last target filename
print("Last dark filename:", darkfile[-1]) #Last dark filename

#d
import astropy.io.fits as fits #import the fits module from astropy.io
#Read in the first object image (0th index)
ny, nx = fits.getdata(datadir + objfile[0] + fext).shape #data array size
print("Data array size:", ny, nx) 

#e
nobj = len(objfile) #Number of object images
ndark = len(darkfile) #Number of dark images
print("Number of object images:", nobj)
print("Number of dark images:", ndark)
print("Number of image rows:", ny)
print("Number of image columns:", nx)
#The counts should not be hardcoded, because the number of images may change in the future.

print("Problem 3")
import numpy as np
#a
objdata = np.zeros((nobj, ny, nx), dtype=np.float64) #Create an empty 3D array to hold the object data  (float64)
darkdata = np.zeros((ndark, ny, nx), dtype=np.float64) #Create an empty 3D array to hold the dark data 
print("Object data array shape:", objdata.shape)
print("Dark data array shape:", darkdata.shape)

#b 
for i in range(nobj): #Populate the object data array with the object images
    objdata[i] = fits.getdata(datadir + objfile[i] + fext) #i works because it is the full range of the number of object images

    if i == nobj - 1: #Store only last header for each set in variable objheader
        objhead = fits.getheader(datadir + objfile[i] + fext)
    

for i in range(ndark): #Populate the dark data array with the dark images
    darkdata[i] = fits.getdata(datadir + darkfile[i] + fext)

    if i == ndark - 1: #Store last header in darkheader
        darkhead = fits.getheader(datadir + darkfile[i] + fext)

#Read the DATE-OBS in those headers
print("Object image date:", objhead['DATE-OBS'])
print("Dark image date:", darkhead['DATE-OBS'])

#Extra Credit --------
#Q: Why not use TIME-OBS?

#TIME-OBS is the time of the observation, but DATE-OBS gives the full date and time of the observation. 
#Using DATE-OBS is generally more informative for understanding when the observations were made, especially if you want to compare observations across different dates.
#The data of an observation tells us things like weather conditions, seasonal effects, and other factors that might influence the data.
#Time doesn't tell more than the time of day that cannot help with those same factors.
#Note here that some headers may include both DATE-OBS and TIME-OBS too since TIME-OBS is outdated for some astronomical data formats.



# %%
