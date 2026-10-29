#Zeina Benton
#Practicum 7
#10/29/26

#%%
print("Problem 1")

import numpy as np


def disk(rad,cent,im): #Copy and paste from Practicum 6 for efficiency
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


def apphot(obj, mask, photrad, inrad, outrad, cent):
    """
    Perform aperture photometry on one star in a 2D image.

    Parameters
    ----------
    obj : 2D array
        Object image.
    mask : 2D Boolean array
        Same shape as obj. True for good pixels, False for bad.
    photrad : float
        Photometry aperture radius in pixels.
    inrad, outrad : float
        Inner and outer sky annulus radii in pixels.
    cent : tuple
        Star center (y, x) in full-image coordinates.
        Use the fitted center from the photometry table.

    Returns
    -------
    flux : float
        Sky-subtracted stellar flux. NaN if the aperture has bad pixels.
    avg : float
        Average sky value per good pixel in the annulus.
    badpx : int
        Number of bad or nonfinite pixels in the aperture.
    """

    if obj.shape != mask.shape: #Flag mismatch shapes
        raise ValueError("Image and mask must have the same shape.")

    if not (0 < photrad < inrad < outrad): #Flags if params are placed in correct order
        raise ValueError("Require 0 < photrad < inrad < outrad.")

    cy, cx = cent 
    ny, nx = obj.shape

    # (a) Copy a subimage enclosing the sky annulus with a margin
    halfsize = int(np.ceil(outrad)) + 1 # halfsize describes how many pixels the cutout extends on either side of center
                     #ceil: always rounds up
    y = int(round(cy)) #Round: rounds to nearest whole number
    x = int(round(cx))

    y0 = int(np.floor(cy - outrad))
    y1 = int(np.ceil(cy + outrad)) + 1
    x0 = int(np.floor(cx - outrad)) #floor: largest integer less than or equal to input
    x1 = int(np.ceil(cx + outrad)) + 1

    if y0 < 0 or x0 < 0 or y1 > ny or x1 > nx: #Flags count is within boundaries
        raise ValueError("Full sky annulus does not fit inside the image.")

    subimage = np.array(obj[y0:y1, x0:x1], dtype=float, copy=True) #C opies object image without changing original image
    good = np.array(mask[y0:y1, x0:x1], dtype=bool, copy=True) # Copies good/bad pixel mask and applies boolean

    # Treat NaN and infinity as bad pixels
    good &= np.isfinite(subimage)

    # Convert the full-image center to subimage coordinates.
    subcenter = (cy - y0, cx - x0)

    # (b) Use disk def twice to create the sky annulus.
    outer = disk(outrad, subcenter, subimage.shape)
    inner = disk(inrad, subcenter, subimage.shape)
    skymask = outer & ~inner & good

    if not np.any(skymask): #Flag if mask went wrong with pixels
        raise ValueError("No good pixels in the sky annulus.")

    # (c) Average only the good sky pixels.
    avg = np.mean(subimage[skymask])

    # (d) Subtract the average sky from the copied subimage.
    subimage -= avg

    # (e) Create the photometry aperture.
    apmask = disk(photrad, subcenter, subimage.shape)

    # Bonus: count bad pixels inside the aperture.
    badpx = int(np.sum(apmask & ~good)) 

    # (f) Sum the sky-subtracted aperture pixels.
    if badpx > 0:  # Flag an aperture containing bad pixels
        flux = np.nan
    else:
        flux = np.sum(subimage[apmask])

    return flux, avg, badpx

# %%
print("Problem 2")

import gaussian as g

coordinates = np.indices((21, 21))

#Noiseless array containing a 2D gaussian
sigma = 2.0
center = (10, 10) #Not given but assumed as the middle index in indices 0 to 20 is 10.
y, x = np.indices((21, 21))

testimage = g.gaussian(
    coordinates,
    width=(2.0, 2.0),
    center=center,
    height=1 / (2 * np.pi * 2.0**2) #Normalized gaussian to flux of 1
)


# All pixels are good
goodmask = np.ones(testimage.shape, dtype=bool)

flux, avg, badpx = apphot(
    testimage, goodmask, 6, 7, 10, center
)

print("Stellar flux:", flux)
print("Average sky:", avg)
print("Bad aperture pixels:", badpx)

"""
Output:
Stellar flux: 0.9868993292420606
Average sky: 1.5810770268095095e-05
Bad aperture pixels: 0

Using the flux normalized to 1 in the gaussian, and the radius of 6 pixels
for the aperture with 3 sigma (6pxl/2pxl = 3 sigma) indicates the aperture
encloses 98.9% of the gaussian. The measured flux found of 0.989 represents that 
and the difference would be from pixel sampling. The average sky would be 
positive and small because it is there is no added sky and the gaussian
gradually smooths with distance and never becoming 0. There were 0 bad pixels
found because there were no nan or inf values, the prompt didn't have any 
bad pixels told to add.
"""
# %%

#Checking the results:
#Code used from demo
import matplotlib.pyplot as plt
y, x = coordinates

apmask = disk(6, center, testimage.shape)
skymask = disk(10, center, testimage.shape) & ~disk(
    7, center, testimage.shape #selects pixels inside the outer disk AND outside the inner disk
)

apim = np.where(apmask, testimage, 0)
anim = np.where(skymask, testimage, 0)

for title, data in [
    ("Aperture Image", apim),
    ("Sky Annulus Image", anim)
]:
    fig = plt.figure(figsize=(10, 4))

    ax2d = fig.add_subplot(121)
    ax2d.imshow(data, origin="lower", cmap="viridis")
    ax2d.set_title(title)
    ax2d.set_xlabel("X pixel")
    ax2d.set_ylabel("Y pixel")

    ax3d = fig.add_subplot(122, projection="3d")
    ax3d.plot_surface(x, y, data, cmap="viridis")
    ax3d.set_xlabel("X pixel")
    ax3d.set_ylabel("Y pixel")
    ax3d.set_zlabel("Intensity")

    plt.tight_layout()
    plt.show()
# %%
