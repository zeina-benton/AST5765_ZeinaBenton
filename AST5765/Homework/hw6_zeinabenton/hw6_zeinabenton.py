#Zeina Benton
#Homework 6
#10/5/26

#%%
import os
import astropy.io.fits as fits
import numpy as np

print("Problem 2")
#a in hw6_zeinabenton_supportfunctions.py

#b
#Retrieve practicum 4 information:
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


#Now begin hw6 new code:
from hw6_zeinabenton_supportfunctions import median_stack_method #Import the median_stack_method function
dark_median = median_stack_method(darkdata) #Median combine the dark images

print("Median dark pixel [217, 184]:", dark_median[217, 184])

#c
dark_header = fits.getheader(os.path.join(datadir, darkfile[0] + fext))
dark_header.add_history("Dark images were median-combined using np.median with axis=0.") #.add_history adds a history entry to the header

#d
fits.writeto( # Write the median-combined dark image to a new fits file
    os.path.join(datadir, "dark_13s_med.fits"),
    dark_median,
    header=dark_header,
    overwrite=True
)

#Additional check here:
saved_data, saved_header = fits.getdata(
    os.path.join(datadir, "dark_13s_med.fits"),
    header=True
)

print("Shape:", saved_data.shape)  # Should be (1024, 1024)
print("Data matches:", np.array_equal(saved_data, dark_median))  # Should be True
print("HISTORY:", saved_header["HISTORY"])  # Should show note

#e 
#Subtract the median dark image from each object image
objdata_darksub = objdata - dark_median[np.newaxis, :, :]  #np.newaxis is used to add a new axis to dark_median so that it can be broadcasted across the object images
#Write first frame to file and save
fits.writeto(
    os.path.join(datadir, "obj_darksub_13s_0.fits"),
    objdata_darksub[0],
    header=objhead,
    overwrite=True
)
#Save fits file in homework file to proper formatting 
fits.writeto(
    "hw6_zeinabenton_prob2_graph1.fits",
    objdata_darksub[0],
    header=objhead,
    overwrite=True
)
print("Before dark subtraction:", objdata[0, 217, 184]) #3D, first 0 means first image, 217 is row, 184 is column
print("After dark subtraction:", objdata_darksub[0, 217, 184])



# %%
