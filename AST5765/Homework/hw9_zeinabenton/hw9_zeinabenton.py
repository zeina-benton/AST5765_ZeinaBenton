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
photometry[0, 0, :2] = [838, 714]  # Frame 0
photometry[0, 1, :2] = [604, 721]  # Frame 1
photometry[0, 2, :2] = [366, 724]  # Frame 2
#Note: [nstar, nframe, first 2 params]

# Star 1
photometry[1, 0, :2] = [327, 713]

# Star 2
photometry[2, 0, :2] = [492, 399]


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
halfsize = 15  # Adjust to include the star while excluding nearby bad pixels

for star in range(nstars): #Loop through all 3 stars
    for frame in range(nframes):
        yguess, xguess = photometry[star, frame, :2] 
        y, x = np.round([yguess, xguess]).astype(int)

        image = flat_corrected[frame]

        # Subarray boundaries
        y0 = max(0, y - radius)
        y1 = min(image.shape[0], y + radius + 1)
        x0 = max(0, x - radius)
        x1 = min(image.shape[1], x + radius + 1)

        # Copy and subtract the local background
        subimage = image[y0:y1, x0:x1].copy()
        subimage -= np.median(subimage)

        # Initial widths, local position, and height
        guess = (
            (3, 3),
            (yguess - y0, xguess - x0),
            subimage.max()
        )

        width, center, height, err = g.fitgaussian(
            subimage, guess=guess
        )

        # Average sigma and position in full-image coordinates
        photometry[star, frame, 2:5] = [
            np.mean(np.abs(width)),
            center[0] + y0,
            center[1] + x0
        ]

# Print the updated table by star
for star in range(nstars):
    print(f"\nStar {star}:")
    print(photometry[star])

# Check fitted positions against guesses
print("\nFitted minus guessed [dy, dx]:")
print(photometry[:, :, 3:5] - photometry[:, :, :2])

# %%
