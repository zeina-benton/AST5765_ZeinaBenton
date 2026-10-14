#Zeina Benton
#practicum 5
#10/14/26

#%%
print("Problem 1")
print("Imports plugged in")
import os
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt
from hw6_zeinabenton_supportfunctions import median_stack_method
from hw7_zeinabenton_supportfunction import *
from practicum5_zeinabenton_supportfunction import *

print("Problem 2")
print("See practicum5_zeinabenton_supportfunction.py for the function normmedcomb")

print("Problem 3")
#HW 7
data = np.loadtxt(
    "hw7_synthetic_transit_lightcurve.csv",
    delimiter=",",
    skiprows=1  # Skip the header
)
time = data[:, 0]  # First column: time in days
flux = data[:, 1]  # Second column: normalized flux

#HW 6
datadir = "hw6_data/" #This is the path to the data directory
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

#Read in the first object image (0th index)
ny, nx = fits.getdata(datadir + objfile[0] + fext).shape #data array size
nobj = len(objfile) #Number of object images
ndark = len(darkfile) #Number of dark images
objdata = np.zeros((nobj, ny, nx), dtype=np.float64) #Create an empty 3D array to hold the object data  (float64)
darkdata = np.zeros((ndark, ny, nx), dtype=np.float64) #Create an empty 3D array to hold the dark data 
for i in range(nobj): #Populate the object data array with the object images
    objdata[i] = fits.getdata(datadir + objfile[i] + fext) #i works because it is the full range of the number of object images

    if i == nobj - 1: #Store only last header for each set in variable objheader
        objhead = fits.getheader(datadir + objfile[i] + fext)
    

for i in range(ndark): #Populate the dark data array with the dark images
    darkdata[i] = fits.getdata(datadir + darkfile[i] + fext)

    if i == ndark - 1: #Store last header in darkheader
        darkhead = fits.getheader(datadir + darkfile[i] + fext)

dark_median = median_stack_method(darkdata) #Median combine the dark images
dark_header = fits.getheader(os.path.join(datadir, darkfile[0] + fext))

#Subtract the median dark image from each object image
objdata_darksub = objdata - dark_median[np.newaxis, :, :]  #np.newaxis is used to add a new axis to dark_median so that it can be broadcasted across the object images

#New code here:
normmedcomb_result, norm_factors = normmedcomb(objdata_darksub, keyword=True, coordinates=(225, 225, -225, -225)) #Normalized median combination of the dark-subtracted object images
#                            hw6 dark-subtracted images      , we want coordinates       ,   y1, x1, y2, x2
print("Combined image shape:", normmedcomb_result.shape)
print("Normalization factors:", norm_factors)
"""
Normalization factors: [10864.  11057.  10536.  
10558.5 11046.  10623.   9916.5  9916.5  9859.5]

"""
fits.writeto(
    os.path.join(datadir, "sky_13s_mednorm.fits"),
    normmedcomb_result,
    header=objhead,
    overwrite=True
)

#Check fits file
saved_data, saved_header = fits.getdata(
    os.path.join(datadir, "sky_13s_mednorm.fits"),
    header=True
)
print("Shape:", saved_data.shape)  # Expected: (1024, 1024)
print("Data matches:", np.array_equal(
    saved_data, normmedcomb_result, equal_nan=True
))  # Expected: True


# %%
