#Zeina Benton
#Practicum 2
#9/18/26

#%%
#1
import numpy as np
print("Q1")

def gaussian_random_generator(N, mu, sigma):
    """
    Generates N random numbers from a Gaussian distribution with mean mu and standard deviation sigma.

    Parameters
    ----------
    N : int
        The number of random numbers to generate.
    mu : float
        The mean of the Gaussian distribution.
    sigma : float
        The standard deviation of the Gaussian distribution.
    Returns
    -------
    random_numbers : array_like
        An array of N random numbers drawn from the specified Gaussian distribution.

    Examples
    -----
    >>> print(gaussian_random_generator(5, 0, 1))
    [ 0.49671415 -0.1382643   0.64768854  1.52302986 -0.23415337]
    >>> print(gaussian_random_generator(3, 10, 2))
    [ 9.76405235 11.16420955  8.14294754]

    """ 
    return np.random.normal(mu, sigma, N)

#2
print("Q2")
print(gaussian_random_generator(10, 55, 13))

#a
results = np.zeros((10, 3))
for x in range(10):
   sample = gaussian_random_generator(10, 55, 13)
   sample_mean = np.mean(sample)
   sample_std = np.std(sample)

   results[x] = [x, sample_mean, sample_std]
print(results)

#3
"""
AI prompt states:
Write a code that creates a subsample containing N random draws from a Gaussian 
distribution with a width σ = 13 and mean μ = 55. Use your code to create a 
sample with N=10 random draws. Do this 10 times (remember, don’t repeat the same 
command!). For each sample, record the sample number (0 to 9), the sample mean, and the 
sample standard deviation in an array with one row per sample. Do not include the actual
 values of the samples in your array. At the end you should have a 10 by 3 array with each line 
 corresponding to one of your samples.
 """

print("AI prompt response:")
mu = 55
sigma = 13

summary = []

for sample_num in range(10):

    draws = np.random.normal(loc=mu, scale=sigma, size=10)

    mean_value = draws.mean()
    1
    std_value = draws.std(ddof=1)

    summary.append([sample_num, mean_value, std_value])

summary = np.array(summary)
print(summary)



#4
with open("practicum2_zeinabenton.txt", "a") as file:
    file.write("# Number of draws per sample: 10\n")
    np.savetxt(file, results, delimiter=",", fmt=["%d", "%.2f", "%.2f"])
    # d = decimal , .2f = floating point number


#5
#N = 100
N_100 = np.zeros((10, 3))
for x in range(10):
   sample = gaussian_random_generator(100, 55, 13)
   sample_mean = np.mean(sample)
   sample_std = np.std(sample)

   N_100[x] = [x, sample_mean, sample_std]
print(N_100)
with open("practicum2_zeinabenton.txt", "a") as f:
    f.write("# Number of draws per sample: 100\n")
    np.savetxt(f, N_100, delimiter=",", fmt=["%d", "%.2f", "%.2f"])


#N=1000
N_1000 = np.zeros((10, 3))
for x in range(10):
    sample = gaussian_random_generator(1000, 55, 13)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample)
    
    N_1000[x] = [x, sample_mean, sample_std]
print(N_1000)
with open("practicum2_zeinabenton.txt", "a") as f:
    f.write("# Number of draws per sample: 1000\n")
    np.savetxt(f, N_1000, delimiter=",", fmt=["%d", "%.2f", "%.2f"])

#N=10000
N_10000 = np.zeros((10, 3))
for x in range(10):
    sample = gaussian_random_generator(10000, 55, 13)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample)
    
    N_10000[x] = [x, sample_mean, sample_std]
print(N_10000)
with open("practicum2_zeinabenton.txt", "a") as f:
    f.write("# Number of draws per sample: 10000\n")
    np.savetxt(f, N_10000, delimiter=",", fmt=["%d", "%.2f", "%.2f"])

#N = 100000
N_100000 = np.zeros((10, 3))
for x in range(10):
    sample = gaussian_random_generator(100000, 55, 13)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample)
    
    N_100000[x] = [x, sample_mean, sample_std]
print(N_100000)
with open("practicum2_zeinabenton.txt", "a") as f:
    f.write("# Number of draws per sample: 100000\n")
    np.savetxt(f, N_100000, delimiter=",", fmt=["%d", "%.2f", "%.2f"])

#N= 1000000
N_1000000 = np.zeros((10, 3))
for x in range(10):
    sample = gaussian_random_generator(1000000, 55, 13)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample)
    
    N_1000000[x] = [x, sample_mean, sample_std]
print(N_1000000)
with open("practicum2_zeinabenton.txt", "a") as f:
    f.write("# Number of draws per sample: 1000000\n")
    np.savetxt(f, N_1000000, delimiter=",", fmt=["%d", "%.2f", "%.2f"])

#%%
#6
"""
For AI:
I need to find the std deviation of the mean for each sample size 
(0 to 9 in txt file 6 times) . So I need my txt read for this 
to be done.
"""

data = np.loadtxt("practicum2_zeinabenton.txt", delimiter=",")
sample_sizes = [10, 100, 1000, 10000, 100000, 1000000]

for i, n in enumerate(sample_sizes):
    mean = data[i*10:(i+1)*10, 1] # second column = mean
    std_of_means = np.std(mean, ddof=1)
    print(f"N = {n}: Standard deviation of means = {std_of_means}")

"""
Next AI:
print the sample size and its calculated standard deviation 
both on the Screen
"""
with open("practicum2_zeinabenton.txt", "a") as f:
    f.write("\n# Sample size Std. dev. of mean\n")

    for i, n in enumerate(sample_sizes):
        means = data[i*10:(i+1)*10, 1]
        std_of_means = np.std(means, ddof=1)

        print(n, std_of_means)
        f.write(f"{n} {std_of_means}\n")

#%%
#7
import matplotlib.pyplot as plt

sample_sizes = []
std_of_means = []

with open("practicum2_zeinabenton.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    parts = line.split()

    if len(parts) == 2:
        try:
            sample_sizes.append(float(parts[0]))
            std_of_means.append(float(parts[1]))
        except ValueError:
            pass

plt.figure(figsize=(8,6))
plt.loglog(sample_sizes, std_of_means, marker='o')

plt.xlabel("Sample Size")
plt.ylabel("Standard Deviation of the Mean")
plt.title("Standard Deviation of the Mean vs. Sample Size")

plt.savefig("practicum2_zeinabenton_loglogplot.png")
plt.show()

# %%
