#Zeina Benton
#Practicum 6
#10/21/26

#%%

print("HW 8, Problem 1")
import numpy as np

def disk(rad,cent,im):
    """
    This functions produces a 2D mask array with the image of a disk.

    Parameters
    -------
    rad: float
        The radius of the disk.
    cent: tuble or 2-length array
        The center of the disk (i.e. (y,x)). Can be fractional.
    im: tuple or 2-length array
        The image shape to make (y,x).

    Returns
    --------
    mask : 2D boolean mask array
        Image of a disk, with True for pixels whose centers are
        within the given radius and False elsewhere.
        
    Notes
    --------
    Order of parameters is important because coordinates and image shape use (y, x) order, and NumPy
    indexes 2D arrays as [row, column].
    
    """
    y, x = np.indices(im) #Creates arrays by (row #, column #)
    mask = (y - cent[0])**2 + (x - cent[1])**2 <= rad**2 #Applies circle equation to every pixel for center

    return mask

from astropy .io import fits

mask = disk(6.2, (12.3, 14.5), (25, 30)) #radius, center, output array structure
fits.writeto("disktest.fits", mask.astype(np.uint8), overwrite=True)

print(mask[14, 14])  # True
print(mask[2, 1])    # False

# %%
print ("HW 8, Problem 2, part a")
import os

#Problem calls the use of k_lampon and k_lampoff data
from hw8_zeinabenton import *
from hw8_zeinabenton.hw6_zeinabenton_supportfunctions import median_stack_method

flatdir = "hw8_zeinabenton/hw6_data/" #directory

lampon_files = [] #Create list to order the files
lampoff_files = []

for filename in sorted(os.listdir(flatdir)): #Sort them in case out of order
    if filename.endswith(".fits"):
        if filename.startswith("rdpharocor_k_lampon"):
            lampon_files.append(filename)
        elif filename.startswith("rdpharocor_k_lampoff"):
            lampoff_files.append(filename)

#Read each set into a 3D array: (image, y, x)
lampon_data = np.array([
    fits.getdata(os.path.join(flatdir, filename))
    for filename in lampon_files
], dtype=float)

lampoff_data = np.array([
    fits.getdata(os.path.join(flatdir, filename))
    for filename in lampoff_files
], dtype=float)

# Median-combine the two sets separately
lampon_median = median_stack_method(lampon_data)
lampoff_median = median_stack_method(lampoff_data)

#Subtract first, then normalize using the previous HW region
flat = lampon_median - lampoff_median #Subtract median stacked flats
norm_factor = np.median(flat[225:-225, 225:-225]) #Previous region
flat = flat / norm_factor #Norm_factor = 20839.0


fits.writeto("flat.fits", flat, overwrite=True)
print("Flat pixel [217, 184]:", flat[217, 184]) #Answer: 1.0277844426316043


print ("HW8, Problem 2, part b")
from hw8_zeinabenton.hw8_zeinabenton import sky_result, objhead

flat_corrected = np.full_like(sky_result, np.nan, dtype=float)
np.divide( #With only primt(flat_corrected[:, 217, 184])), it gave error for indivisible by 0
    sky_result,
    flat,
    out=flat_corrected,
    where=np.isfinite(flat) & (flat != 0) #Looking for true values where flat is not 0 and not nan or inf
)
print(flat_corrected[:, 217, 184])
#Answer: [-57.77651881  98.84923307  75.04854138 207.09383493 130.13870669
#           7.94926324  58.99616137 -51.92203828 -35.76731818]

flat_header = objhead.copy() #Don't want to overwrite objhead on accident
flat_header.add_history("Sky_subtracted frames now Flat-field corrected using flat.fits.")

fits.writeto(
    "stars_13s_9_flat.fits",
    flat_corrected[-1], #Save last frame
    header=flat_header,
    overwrite=True
)

# %%
