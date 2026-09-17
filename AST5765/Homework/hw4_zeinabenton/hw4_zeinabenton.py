#Zeina Benton
#HW4
#9/17/26

#%%
from hw4_zeinabenton_support_functions import gaussian_random_generator

print ("Question 2: The Gaussian distribution in Python")

#a
N = 10000
mu = 55
sigma = 13

gaussian_sample = gaussian_random_generator(N, mu, sigma)
print("The Gaussian sample for part a is: ", gaussian_sample)
# %%
