#Zeina Benton
#Final Project
#11/23/26

#%%
import numpy as np
import gaussian as g
from project_zeinabenton_supportfunctions import splinterp

print("Problem 1")
#Write a routine, listed as splinterp
# Establish parameters; calling function
mag = 5.0 
lo = -2.0
hi = 2.0
shift = -0.2

xold = np.linspace(lo, hi, int(np.round(hi - lo + 1))) # Makes evenly spaced points and includes both endpoints
xnew = np.linspace(lo, hi, int(np.round((hi - lo) * mag + 1))) + shift

yold = g.gaussian(xold)
ynew = splinterp(xnew, xold, yold)


# %%
print("Problem 2")

# Example testing:
# 41 points with spacing 0.1.
x_test_old = np.linspace(-2.0, 2.0, 41)

# 181 points with spacing 0.02, shifted by -0.025.
x_test_new = np.linspace(-1.8, 1.8, 181) - 0.025

y_test_old = g.gaussian(x_test_old, width=1.0, center=0.35, height=1.0)
y_test_new = splinterp(x_test_new, x_test_old, y_test_old)
y_expected = g.gaussian(x_test_new, width=1.0, center=0.35, height=1.0)

max_error = np.max(np.abs(y_test_new - y_expected))
print(f"Maximum absolute error: {max_error:.3e}")
assert max_error < 1e-5, "Spline interpolation and shifting test failed"

"""
I tested definition splinterp using a Gaussian sampled at 41 points spaced 0.1 
units apart. I evaluated the spline on a finer grid with spacing 0.02 and 
shifted the grid by −0.025 units, one quarter of the original sample spacing. 
I calculated the expected values by evaluating the Gaussian directly at the 181 
shifted positions. The maximum absolute difference was \(7.75\times10^{-7}\), 
below the test tolerance of \(10^{-5}\). Because every shifted position fell
 between original sample locations, the test required the routine to estimate values 
 between samples. The error is the pass/fail check. Omitting the shift increased 
 the maximum error to \(1.52\times10^{-2}\). 

"""
# %%
print("Problem 3")
#Written routine for interp_xcorr

print("Problem 4")
from project_zeinabenton_supportfunctions import interp_xcorr

#Example testing:

pixels = np.arange(512) # Generate an array of pixel indices from 0 to 511
expected_shift = 0.347 # Shift in pixels to test the cross-correlation routine
tolerance = 0.01 # Tolerance for the shift measurement

reference = g.gaussian(pixels, width=3.0, center=200.0, height=1.0) # Generate a reference Gaussian spectrum centered at pixel 200
spectrum = g.gaussian(
    pixels, width=3.0, center=200.0 + expected_shift, height=1.0
) # Generate a spectrum that is the same Gaussian but shifted by expected_shift

# Execute the cross-correlation routine to measure the shift
measured = interp_xcorr(spectrum, reference, oversample=10, max_lag=2.0)
reversed_shift = interp_xcorr(reference, spectrum, oversample=10, max_lag=2.0)

# Calculate the absolute errors for both forward and reverse measurements
forward_error = abs(measured - expected_shift) # How close the routine got to the known shift
reverse_error = abs(reversed_shift + expected_shift) # Checks that switching which spectrum is the reference flips the sign and still gives the right magnitude.

print(f"Forward: expected {expected_shift:+.6f}, measured {measured:+.6f} pixels")
print(f"Reverse: expected {-expected_shift:+.6f}, measured {reversed_shift:+.6f} pixels")
print(f"Absolute errors: {forward_error:.6f}, {reverse_error:.6f} pixels")

assert forward_error < tolerance, "Forward shift test failed"
assert reverse_error < tolerance, "Reverse shift test failed"
print("Cross-correlation test passed.")

"""
I tested the interpolated cross-correlation routine using two 
Gaussian profiles sampled. The reference peak was centered at 
pixel 200.000, and the second peak was centered at pixel 200.347,
 giving a known offset of +0.347 pixels. I used 10* sigma oversampling 
 and searched lags within ±2 pixels. The routine recovered a shift 
 of +0.346397 pixels, with an absolute error of 0.000603 pixels. 
 Swapping the inputs returned −0.346397 pixels, confirming the sign
convention. Both results were within the 0.01-pixel tolerance. 
The test also checked the Gaussian refinement. Returning the best
 grid lag of +0.300 pixels would give an error of 0.047 pixels, 
 exceeding the 0.01-pixel tolerance.The forward grid peak alone was 
 +0.300 pixels, which would have failed the test.


"""
# %%

print("Problem 5")

import numpy as np
from astropy.io import fits

# Read in the bias files and stack them into a 3D array
import numpy as np
from astropy.io import fits

bias_files = [f"galaxy/data/bs{number:03d}n.fits" for number in range(334, 344)]
bias_stack = np.stack([fits.getdata(filename) for filename in bias_files])

master_bias = np.median(bias_stack, axis=0).astype(np.float32)

fits.writeto("master_bias.fits", master_bias, overwrite=True)
print("Master bias pixel [150, 150]:", master_bias[150, 150])

"""
Output:

 Problem 5
Master bias pixel [150, 150]: 0.5

"""
# %%
print("Problem 6")

flat_files = [f"galaxy/data/bs{number:03d}n.fits" for number in range(324, 334)]
flat_stack = np.stack([fits.getdata(filename) for filename in flat_files])

# Subtract the master bias from each dome flat.
flat_corrected = flat_stack - master_bias

# Divide each flat by its own median to put them on the same scale.
flat_medians = np.median(flat_corrected, axis=(1, 2), keepdims=True)
normalized_flats = flat_corrected / flat_medians

# Take the median across exposures at each pixel.
master_flat = np.median(normalized_flats, axis=0)

# Set the final image's median to 1 and save as 32-bit floating point.
master_flat /= np.median(master_flat)
master_flat = master_flat.astype(np.float32)

fits.writeto("master_flat.fits", master_flat, overwrite=True)
print("Master flat pixel [150, 150]:", master_flat[150, 150])

"""
Output:
Problem 6
Master flat pixel [150, 150]: 0.94663507
"""
# %%
print("Problem 7")

galaxy_image = fits.getdata("galaxy/data/bs397n.fits") # 600-second exposure of UGC 9039
lamp_image = fits.getdata("galaxy/data/bs395n.fits") # The NeAr lamp exposure associated with UGC 9039

# Subtract the bias first, then divide by the flat field.
galaxy_corrected = ((galaxy_image - master_bias) / master_flat).astype(np.float32)
lamp_corrected = ((lamp_image - master_bias) / master_flat).astype(np.float32)

fits.writeto("galaxy_corrected.fits", galaxy_corrected, overwrite=True)
fits.writeto("lamp_corrected.fits", lamp_corrected, overwrite=True)

print("Corrected galaxy pixel [150, 150]:", galaxy_corrected[150, 150])
print("Corrected lamp pixel [150, 150]:", lamp_corrected[150, 150])

"""
Output:
Problem 7
Corrected galaxy pixel [150, 150]: 49.121357
Corrected lamp pixel [150, 150]: 16.373787

"""
# %%

print("Problem 8")

# Plot the brightness profile
import matplotlib.pyplot as plt

brightness = np.median(galaxy_corrected, axis=1)
rows = np.arange(brightness.size)

plt.plot(rows, brightness)
plt.xlabel("Row index (y)")
plt.ylabel("Median brightness")
plt.title("UGC 9039 spatial brightness profile")
plt.grid(alpha=0.3)

plt.savefig("galaxy_brightness_profile.png", dpi=300)
plt.show()

# Focus and mark the galaxy region
first_good_row = 20 # Cut out the detector-edge or calibration effects
last_good_row = 268 # Cut out the detector-edge or calibration effects
galaxy_lower = 60 # Captures the main peak of the galaxy flux
galaxy_upper = 235 

brightness_clean = brightness.copy() # Copy to avoid modifying the original brightness array
brightness_clean[:first_good_row] = 0 # Zero the messy edges
brightness_clean[last_good_row + 1:] = 0

# Search only usable rows so a zeroed edge cannot be picked as the peak.
usable_rows = brightness_clean[first_good_row:last_good_row + 1]
galaxy_y = first_good_row + np.argmax(usable_rows)

plt.plot(rows, brightness_clean)
plt.axvspan(galaxy_lower, galaxy_upper, alpha=0.2, label="Galaxy flux region") # plt.axvspan() shades a range on the plot.
plt.axvline(galaxy_y, color="black", linestyle="--", label="Galaxy center")
plt.xlabel("Row index (y)")
plt.ylabel("Median brightness")
plt.title("UGC 9039 spatial brightness profile with edges zeroed")
plt.legend()

plt.savefig("galaxy_brightness_profile_cleaned.png", dpi=300)
plt.show()

print("Lower galaxy row:", galaxy_lower)
print("Upper galaxy row:", galaxy_upper)
print("Galaxy center y-index:", galaxy_y)

"""
Output:
Problem 8
Lower galaxy row: 60
Upper galaxy row: 235
Galaxy center y-index: 139

"""
# %%
print("Problem 9")


stripe_height = 5 # Horizontal stripe height
half_height = stripe_height // 2 # Find middle row of a stripe

# Align the stripes so galaxy_y is the middle row of one stripe.
center_stripe_start = galaxy_y - half_height
stripe_start = first_good_row + (
    (center_stripe_start - first_good_row) % stripe_height
)

# Keep only complete stripes within the usable detector rows.
n_stripes = (last_good_row + 1 - stripe_start) // stripe_height # Figure out how many full 5-row stripes fit and where to stop slicing.
stripe_stop = stripe_start + n_stripes * stripe_height

# Group the image into (stripe, row within stripe, wavelength pixel).
n_columns = galaxy_corrected.shape[1]
stripes = galaxy_corrected[stripe_start:stripe_stop, :].reshape(
    n_stripes, stripe_height, n_columns
)

# Take the median of the five rows at each wavelength pixel.
galaxy_reduced = np.median(stripes, axis=1)

# Converts the original image row to a stripe index
reference_row = (galaxy_y - stripe_start) // stripe_height # Find which stripe contains the galaxy center row
reference_spectrum = galaxy_reduced[reference_row] # Extract the reference spectrum from the reduced image

print("Number of rows in reduced image:", galaxy_reduced.shape[0])
print("Reference spectrum row index:", reference_row)

"""
Output: 
Number of rows in reduced image: 49
Reference spectrum row index: 23

"""
plt.figure() # Shows all the extracted spectra as a 2D image
plt.imshow(galaxy_reduced, origin="lower", aspect="auto", cmap="gray")
plt.axhline(reference_row, color="orange", linestyle="--", label="Reference row")
plt.xlabel("Wavelength pixel")
plt.ylabel("Stripe index")
plt.title("UGC 9039 reduced spectral image")
plt.colorbar(label="Median signal")
plt.legend()

plt.savefig("galaxy_reduced_spectra.png", dpi=300)
plt.show()

plt.figure() # Shows just the spectrum from that center stripe
plt.plot(np.arange(n_columns), reference_spectrum)
plt.xlabel("Wavelength pixel")
plt.ylabel("Median signal")
plt.title(f"UGC 9039 reference spectrum (stripe {reference_row})")

plt.savefig("galaxy_reference_spectrum.png", dpi=300)
plt.show()

# %%
print("Problem 10")

# Extract galaxy spectra from the reduced image; locate it
sky_low = 240
sky_high = 259

# 2D galaxy image before sky subtraction
plt.figure()
plt.imshow(galaxy_corrected, origin="lower", aspect="auto", cmap="gray")
plt.axhspan(sky_low - 0.5, sky_high + 0.5, alpha=0.25)
plt.xlabel("Wavelength pixel")
plt.ylabel("Original row index")
plt.title("UGC 9039 with sky rows marked")

plt.savefig("galaxy_sky_rows.png", dpi=300)
plt.show()

# Make new image
sky_image = galaxy_corrected[sky_low:sky_high + 1, :].copy()

# Median combine the sky rows to make a 1D spectrum, reduce bad pixels to NaN
sky_image[~np.isfinite(sky_image)] = np.nan
sky_spectrum = np.nanmedian(sky_image, axis=0)

print("Low sky row:", sky_low)
print("High sky row:", sky_high)
"""
Output:
Low sky row: 240
High sky row: 259
"""

# New image of sky subtracted galaxy
plt.figure()
plt.plot(sky_spectrum)
plt.xlabel("Wavelength pixel")
plt.ylabel("Median sky signal")
plt.title("Sky-subtracted Galaxy Spectrum")

plt.savefig("galaxy_sky_subtracted_spectrum.png", dpi=300)
plt.show()


# %%
