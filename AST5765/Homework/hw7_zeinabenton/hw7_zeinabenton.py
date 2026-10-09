#Zeina Benton
#HW 7
#10/8/26

#%%
import numpy as np
import matplotlib.pyplot as plt

print("Problem 3:")
#a
data = np.loadtxt(
    "hw7_synthetic_transit_lightcurve.csv",
    delimiter=",",
    skiprows=1  # Skip the header
)
time = data[:, 0]  # First column: time in days
flux = data[:, 1]  # Second column: normalized flux

#Plot:
plt.figure(figsize=(8, 5))
plt.scatter(time, flux, s=10, color="black", linewidths=0)

plt.xlabel("Time (days)", fontsize=13)
plt.ylabel("Normalized flux", fontsize=13)
plt.title("Synthetic Transit Lightcurve", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.tick_params(which="both", direction="in", top=True, right=True)
plt.minorticks_on()
plt.tight_layout()

plt.savefig("hw7_zeinabenton_prob2_plot1.png", dpi=300)
plt.show()

#b
#i
from hw7_zeinabenton_supportfunction import box_window
from scipy.optimize import curve_fit #curve fitting function

#ii
# Estimate starting parameters from the observed transit dip
depth = 1.0 - np.min(flux) #depth is most likely the difference between the normalized flux (1.0) and the minimum observed flux
#Note, this could be a noisy measurement, so it may overestimate the actual depth.
dip = flux < 1.0 - depth / 2 #The dip is the bottom of the box, where the flux is less than half the depth of the transit

center = (np.min(time[dip]) + np.max(time[dip])) / 2
width = np.max(time[dip]) - np.min(time[dip])

p0 = [center, width, depth] #This is the initial guess for the parameters: center, width, and depth of the transit.
popt, pcov = curve_fit( #Curve fitting function that fits the box_window model to the observed data
    box_window, #The def
    time,
    flux,
    p0=p0, #Means the initial guess for the parameters is p0
    bounds=( #Bounds for the parameters: center, width, and depth
        [np.min(time), 0, 0],
        [np.max(time), np.ptp(time), 1] #np.ptp(time) is the range of the time values, which is the maximum minus the minimum
    )
)

center_fit, width_fit, depth_fit = popt

print("Starting parameters:", p0) #p0 is a list of the starting parameters
print("Fitted parameters:", popt) #popt is a list of the fitted parameters
#This fit can’t trusted from this code alone. 
# p0 contains starting guesses; popt contains what the optimizer returned. 
# A successful call does not establish that it found the best fit.
# It only establishes that it found a local minimum in the parameter space.


#iii
#Finding the radius of the planet using the fitted depth and the formula Rp = Rstar * sqrt(depth)
stellar_radius = 1.14 #Given in the problem
planet_radius = stellar_radius * np.sqrt(depth_fit) #1.14 given in the problem 
print(f"Transit center: {center_fit:.6f} days")
print(f"Transit width: {width_fit:.6f} days")
print(f"Transit height/depth: {depth_fit:.6f}")
print(f"Planet radius: {planet_radius:.6f} solar radii")

#iv
#Plot the fitted model over the data
left = center_fit - width_fit / 2 # Exact box edges for plotting
right = center_fit + width_fit / 2

model_time = [ 
    np.min(time), left, left,
    right, right, np.max(time)
]
model_flux = [
    1, 1, 1 - depth_fit,
    1 - depth_fit, 1, 1
]

plt.figure(figsize=(8, 5))
plt.scatter(time, flux, s=12, color="black",
            linewidths=0, label="Observations")
plt.plot(model_time, model_flux, color="red",
         linewidth=1.5, label="Fitted box model")

plt.xlabel("Time (days)", fontsize=13)
plt.ylabel("Normalized flux", fontsize=13)
plt.title("Synthetic Transit Lightcurve with Fitted Box Model", fontsize=12)
plt.tick_params(which="both", direction="in",
                top=True, right=True, labelsize=11)
plt.minorticks_on()
plt.legend(frameon=False)
plt.tight_layout()

plt.savefig("hw7_zeinabenton_prob2_graph2.png", dpi=300)
plt.show()

#c
#Given errors:
stellar_radius_error = 0.01
depth_error = 0.002

planet_radius_error = np.sqrt(
    (np.sqrt(depth_fit) * stellar_radius_error)**2
    + (stellar_radius * depth_error / (2 * np.sqrt(depth_fit)))**2
) #Uncertainty in quadrature

print(f"Planet radius error: {planet_radius_error:.6f} solar radii")
# %%
