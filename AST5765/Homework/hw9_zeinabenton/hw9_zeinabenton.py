#Zeina Benton
#HW 9
#10/21/26

#%%
from Practicum6_zeinabenton import *

print("HW9, Problem 2")
import numpy as np
#Variables
nstars = 3 #3 stars
nframes = 9  #9 frames, (9, 1024, 1024)
nparameters = 7 #given in assignment a-g

print("Stellar photometry:")
print("Parameters: yguess, xguess, star_w, cy, cx, star_flx, sky_avg")

photometry = np.full((nstars, nframes, nparameters), np.nan) #Putting in nan placeholders not 0

for i in range(3):
    print(f"Star {i}:")
    print(photometry[i])
    print()  # Blank line between stars

"""
Stellar photometry:
Parameters: yguess, xguess, star_w, cy, cx, star_flx, sky_avg
Star 0:
[[nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]]

Star 1:
[[nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]]

Star 2:
[[nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]
 [nan nan nan nan nan nan nan]]
"""
#Fill in the position of star 0 in the other two frames.

# %%
