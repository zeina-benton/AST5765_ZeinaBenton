#Zeina Benton
#HW 10
#11/6/26

#%%
print("HW10, Problem 2")

from practicum7_zeinabenton.practicum7_zeinabenton import apphot
from hw9_zeinabenton.hw9_zeinabenton import ( #Import variables
    photometry,
    flat_corrected,
    aperture_radius,
    sky_inner_radius,
    sky_outer_radius
)

def dophot(frames, mask, photrad, inrad, outrad):
    """
    Takes input with 3D array of observational frames, mask, radius
    of photometry aperature, and inner and outer radii.

    Parameters
    ----------
    frames : 3D array
        Observational frames of stars.
    mask : 2D Boolean array
        Same shape as frames. True for good pixels, False for bad.
    photrad : float
        Photometry aperture radius in pixels.
    inrad, outrad : float
        Inner and outer sky annulus radii in pixels.

    Returns
    -------
    phot : 3D array
        Table of photometry results for each star in each frame.
    
    Example
    -------
    >>> phot = dophot(frames, mask, photrad, inrad, outrad)
    
    """
    phot = photometry.copy() #Copy the hw9 table, don't want to accidentally overwrite it
    nstars, nframes = phot.shape[:2]

    for star in range(nstars): 
        for frame in range(nframes):
            center = tuple(phot[star, frame, 3:5]) #Find the center of the star in the frame

            flux, avg, badpx = apphot(  #def from Hw10
                frames[frame], mask, photrad, inrad, outrad, center
            )

            phot[star, frame, 5] = flux
            phot[star, frame, 6] = avg

    return phot

print("HW10, Problem 3 (says 4 on assignment)")
import numpy as np

# Full-image mask: True for pixels finite in all frames being measured
# Different than mask from practicum 6 disk definition
mask = np.all(
    np.isfinite(flat_corrected[:photometry.shape[1]]),
    axis=0
)

phot = dophot( #Call the function to perform photometry on the stars from the table
    flat_corrected,
    mask,
    aperture_radius,
    sky_inner_radius,
    sky_outer_radius
)

np.savetxt(
    "hw10_zeinabenton_photometry.txt",
    phot.reshape(-1, phot.shape[-1]),
    header="yguess xguess width cy cx star_flux sky_avg",
    fmt="%.8f"
)

# %%
