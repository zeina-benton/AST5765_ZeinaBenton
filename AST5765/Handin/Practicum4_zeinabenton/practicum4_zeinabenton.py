#Zeina Benton
#Practicum 4
#10/1/26

#%%
print("Problem 2")
#a
import os
datadir = "/Users/zeinabenton/Desktop/AST5765/AST5765_ZeinaBenton/AST5765_ZeinaBenton-1/AST5765/Handin/Practicum4_zeinabenton/hw6_data/" #This is the path to the data directory
fext = ".fits" #This is the file extension of the data files

objprefix = "rdpharocor_stars_13s_" #Prefix for the object images for fits compliant
darkprefix = "rdpharocor_dark_13s_" #Prefix for the dark images for fits compliant

#B
objfile = []
darkfile = []

for filename in sorted(os.listdir(datadir)):
    if filename.endswith(fext):
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
data = fits.getdata(datadir + objfile[0] + fext) #Read in the first object image (0th index)
ny, nx = data.shape #data array size
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


# %%
