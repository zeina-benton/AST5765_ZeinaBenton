#Zeina Benton
#HW5
#9/25/26

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Problem 2: ")
#This is from Practicum 3.
poisson_data = np.random.poisson(lam=10000, size=396) #randomly generate 396 Poisson-distributed numbers
uniform_data = np.random.uniform(0, 1e6, size=4)
array = np.concatenate((poisson_data, uniform_data)) #The sub-sample 

arr_mean = np.mean(array)
arr_med = np.median(array)
#b
arr_std = np.std(array)

mask = array[np.abs(array - arr_med) < 5*arr_std]
print("Mean of sub-sample =", np.mean(mask))
print("Median of sub-sample =", np.median(mask))
print("Std Dev of sub-sample =", np.std(mask))
#-------------
#Sub-sub sample of Problem 2 begins here:
sub_mean = np.mean(mask)
sub_med = np.median(mask)
sub_std = np.std(mask)
sub_mask = mask[np.abs(mask - sub_med) < 5*sub_std]
print("Mean of sub-sub-sample =", np.mean(sub_mask))
print("Median of sub-sub-sample =", np.median(sub_mask))
print("Std Dev of sub-sub-sample =", np.std(sub_mask))



# %%
