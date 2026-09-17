#Zeina Benton
#HW4
#9/17/26

#%%
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt 
from hw4_zeinabenton_support_functions import gaussian_random_generator, gaussian

print ("Question 2: The Gaussian distribution in Python")

#a
N = 10000
mu = 55
sigma = 13

gaussian_sample = gaussian_random_generator(N, mu, sigma)
print("The Gaussian sample for part a is: ", gaussian_sample)

#b
plt.figure(figsize=(10, 6))
plt.hist(gaussian_sample, bins = np.arange(0, 101, 1), alpha=0.7, color='blue')
plt.xlabel('x')
plt.ylabel('N(x)')
plt.title('Histogram of Gaussian Sample (N=10,000, mu=55, sigma=13)')

plt.savefig('hw4_zeinabenton_problem2b_plot1.png')
plt.show()

#c
x = np.arange(0.5, 100.5, 1) #center of each bin

plt.figure(figsize=(10, 6))
plt.hist(gaussian_sample, bins = np.arange(0, 101, 1), alpha=0.7, color='blue')
plt.plot(x, N * gaussian(x, mu, sigma), color='red', linewidth=2, label='Gaussian PDF') #new addition
plt.xlabel('x')
plt.ylabel('N(x)')
plt.title('Histogram of Gaussian Sample (N=10,000, mu=55, sigma=13) with Gaussian PDF')

plt.savefig('hw4_zeinabenton_problem2c_plot2.png')
plt.show()


#---------------------------------






# %%
