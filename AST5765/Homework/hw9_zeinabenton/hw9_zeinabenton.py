#Zeina Benton
#HW 9
#10/21/26

#%%
from Practicum6_zeinabenton import *

print("HW9, Problem 2")
import numpy as np
#Variables
nstars = 3 #3 stars
nframes = 3 #3 frames per star
nparameters = 7 #given in assignment a-g

print("Stellar photometry:")
print("Parameters: yguess, xguess, star_w, cy, cx, star_flx, sky_avg")

photometry = np.full((nstars, nframes, nparameters), np.nan) #Putting in nan placeholders not 0

for star in range(nstars):
    print(f"Star {star}:")
    for frame in range(nframes):
        print(f"Frame {frame}: {photometry[star, frame]}")
    print()

"""
Stellar photometry:
Parameters: yguess, xguess, star_w, cy, cx, star_flx, sky_avg
Star 0:
Frame 0: [nan nan nan nan nan nan nan]
Frame 1: [nan nan nan nan nan nan nan]
Frame 2: [nan nan nan nan nan nan nan]

Star 1:
Frame 0: [nan nan nan nan nan nan nan]
Frame 1: [nan nan nan nan nan nan nan]
Frame 2: [nan nan nan nan nan nan nan]

Star 2:
Frame 0: [nan nan nan nan nan nan nan]
Frame 1: [nan nan nan nan nan nan nan]
Frame 2: [nan nan nan nan nan nan nan]

"""
#Fill in the position of star 0 in the other two frames (guesses)
# Star 0
photometry[0, 0, :2] = [835.13606, 715.90404]  # Frame 0
photometry[0, 1, :2] = [602, 719]  # Frame 1 
photometry[0, 2, :2] = [364.392, 725.544]  # Frame 2 
#Note: [nstar, nframe, first 2 params]

# Star 1
photometry[1, 0, :2] = [569.4, 282.6] 

# Star 2
photometry[2, 0, :2] = [669, 522] 


nstars, nframes, nparameters = photometry.shape #Query table shape for nstars and nframes

#Calculate the offset of star 0 between frames 0 and 1
offset_01 = photometry[0, 1, :2] - photometry[0, 0, :2]

# Apply that offset to stars 1 and 2
for star in range(1, nstars):
    photometry[star, 1, :2] = photometry[star, 0, :2] + offset_01

#Calculate the offset of star 0 between frames 0 and 2 
offset_02 = photometry[0, 2, :2] - photometry[0, 0, :2]

# Apply that offset to stars 1 and 2
for star in range(1, nstars):
    photometry[star, 2, :2] = photometry[star, 0, :2] + offset_02

#Print the updated table
print("Stellar photometry:")
print("Parameters: yguess, xguess, star_w, cy, cx, star_flx, sky_avg")
for star in range(nstars):
    print(f"\nStar {star}:")
    print(photometry[star])

"""
Stellar photometry:
Parameters: yguess, xguess, star_w, cy, cx, star_flx, sky_avg

Star 0:
[[838. 714.  nan  nan  nan  nan  nan]
 [604. 721.  nan  nan  nan  nan  nan]
 [366. 724.  nan  nan  nan  nan  nan]]

Star 1:
[[ 327.  713.   nan   nan   nan   nan   nan]
 [  93.  720.   nan   nan   nan   nan   nan]
 [-145.  723.   nan   nan   nan   nan   nan]]

Star 2:
[[492. 399.  nan  nan  nan  nan  nan]
 [258. 406.  nan  nan  nan  nan  nan]
 [ 20. 409.  nan  nan  nan  nan  nan]]
"""

# %%
print("HW9, Problem 3, Part A")
import gaussian as g 
from astropy.io import fits

#Retrieve flat corrected image and apply to stars
from Practicum6_zeinabenton.practicum6_zeinabenton import flat_corrected

#Estimate the 1σ widths and location of each star 
nstars, nframes = photometry.shape[:2]
radius = 15 # Half-size of the subarray; adjust after inspecting the stars

for star in range(nstars): #Loop through all stars
    for frame in range(nframes):

        image = flat_corrected[frame] #Apply flat corrected image to star 
        yguess, xguess = photometry[star, frame, :2]

        # Clear any previous fit results
        photometry[star, frame, 2:5] = np.nan

        # Check the guess is inside the image
        ny, nx = image.shape
        if not (0 <= yguess < ny and 0 <= xguess < nx):
            print(f"Star {star}, frame {frame}: check position guess")
            continue
        y, x = np.round([yguess, xguess]).astype(int)

        # Boundaries of a small subarray around the star
        y0 = max(0, y - radius)
        y1 = min(ny, y + radius + 1)
        x0 = max(0, x - radius)
        x1 = min(nx, x + radius + 1)

        # Copy the subarray so subtraction does'nt change the original
        subimage = image[y0:y1, x0:x1].copy() 

        if not np.all(np.isfinite(subimage)):
            print(f"Star {star}, frame {frame}: adjust cutout to avoid NaN/inf")
            continue

        # Subtract the median for an approximately zero background
        subimage -= np.median(subimage) 

        # Initial guesses: two sigmas, local center, peak height
        guess = (
            (3.0, 3.0),
            (yguess - y0, xguess - x0),
            subimage.max()
        )

         # Fit the Gaussian to the subarray, width found here within 1sigma
        width, center, height, err = g.fitgaussian(
            subimage,
            lsargs={"maxfev": 10000}
        )

        # Finding cy,cx: star position 
        photometry[star, frame, 2] = np.mean(np.abs(width))
        photometry[star, frame, 3] = center[0] + y0
        photometry[star, frame, 4] = center[1] + x0

# Print the updated table
print("\nColumns: yguess, xguess, width, cy, cx, star, sky")

for star in range(nstars): #Print table out with nstars and nframe again
    print(f"\nStar {star}:")
    print(photometry[star])

# Compare fitted coordinates with the original guesses
print("\nPosition differences: fitted minus guessed [dy, dx]")

for star in range(nstars):
    print(f"\nStar {star}:")
  
    print(photometry[star, :, 3:5] - photometry[star, :, :2])

"""
Fitted positions agree with the initial guesses within 2.7 pixels
in each coordinate. Each star's fitted widths are similar across
the three frames.

Columns: yguess, xguess, width, cy, cx, star, sky

Star 0:
[[835.13606    715.90404      1.45873082 836.98300798 713.59112165
           nan          nan]
 [602.         719.           1.39711195 602.82167881 718.72163459
           nan          nan]
 [364.392      725.544        1.45956387 366.79937358 723.09390731
           nan          nan]]

Star 1:
[[569.4        282.6          1.07730267 568.25810469 283.30271154
           nan          nan]
 [336.26394    285.69596      0.97642406 333.95994341 288.36021444
           nan          nan]
 [ 98.65594    292.23996      1.11013401  98.07103802 292.89930248
           nan          nan]]

Star 2:
[[669.         522.           1.04508285 667.88216851 520.22577065
           nan          nan]
 [435.86394    525.09596      0.98241272 433.57879503 525.30506284
           nan          nan]
 [198.25594    531.63996      1.17441291 197.63687521 529.79165967
           nan          nan]]

Position differences: fitted minus guessed [dy, dx]

Star 0:
[[ 1.84694798 -2.31291835]
 [ 0.82167881 -0.27836541]
 [ 2.40737358 -2.45009269]]

Star 1:
[[-1.14189531  0.70271154]
 [-2.30399659  2.66425444]
 [-0.58490198  0.65934248]]

Star 2:
[[-1.11783149 -1.77422935]
 [-2.28514497  0.20910284]
 [-0.61906479 -1.84830033]]

"""

# %%
print("HW9, Problem 3, Part B")

# Average all fitted widths into one sigma for the dataset
sigma = np.mean(photometry[:, :, 2])
print("Average sigma:", sigma)

aperture_radius = 3 * sigma
sky_inner_radius = 5 * sigma
sky_outer_radius = 8 * sigma

subimage_size = int(20 * sigma) #To slice an image this must be an integer

print("Aperture radius:", aperture_radius)
print("Sky annulus radii:", sky_inner_radius, sky_outer_radius)
print("Subimage size:", subimage_size)

"""
#A 3 sigma aperture contains about 99% of an ideal Gaussian distribution
# therefore the aperature should be most accurate to balance the target star's light with background noise.

#My sigma is 1.19 pixels, so the sky annulus radii needs to cover
# beyond that to estimate the local sky and contain more pixels. 
#There being 2 sky annulus radii, this implies and inner and out annulus.
#  I figure 5 sigma covers the inner, and 8 sigma covers the outer sky containing any bad pixels and noise.
# It is far enough away from the target stars to not get confused.
The inner sky annulus is 5.93 and outer sky annulus is 9.50

# The subimage must be big enough to contain all of the annuli and the aperature, therefore
# bigger than 16 sigma, the outer sky annulus diameter.
# I made it 20 sigma as that is bigger than the outer sky annulus 
to represent the full sub-image. It is 23x23 pixels.


"""
# %%
