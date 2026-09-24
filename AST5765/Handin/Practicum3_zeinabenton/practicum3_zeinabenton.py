#Zeina Benton
#Practicum 3
#9/25/26

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Problem 1:")
#a
model1 = []
model2 = []

current = model1

with open("practicum3_1.dat") as f:
    for line in f:

        if "#Model 2" in line:
            current = model2
            continue

        if line.startswith("#"):
            continue

        current.append(line.split())

model1 = pd.DataFrame(model1, columns=["x", "f(x)"]).astype(float)
model2 = pd.DataFrame(model2, columns=["x", "f(x)"]).astype(float)


plt.figure(figsize=(6,6))
plt.plot(model1["x"], model1["f(x)"], "o", label="Model 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("F(x) vs x Plot")
plt.legend()
plt.savefig("practicum3_zeinabenton_prob1a_plot1.png")
plt.show()

#b
import linfit as L
x = model1["x"]
y = model1["f(x)"]
sigma = np.full(len(y), 0.5) #uncertainty, np.full creates an array of the same length as y

(af, bf, a_unc, b_unc, chisq, prob, covar, yfit) = \
L.linfit(y, x, y_unc=sigma)

print("intercept =", af, "+/-", a_unc)
print("slope =", bf, "+/-", b_unc)

#check if within 3 sigma of true values
a_true = 1.2 # true intercept
b_true = 3.2 # true slope
print(abs(af - a_true) < 3*a_unc)
print(abs(bf - b_true) < 3*b_unc)

plt.figure(figsize=(6,6))
plt.plot(x, y, "o", label="data")
plt.plot(x, yfit, label="fit")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("F(x) vs x Plot of Linear Fit to Model 1")
plt.legend()
plt.savefig("practicum3_zeinabenton_prob1b_plot2.png")
plt.show()


#c
print("chi-square =", chisq)
print("probability =", prob)
#Plot saved above in part b.


#d
plt.figure(figsize=(6,6))
plt.plot(model2["x"], model2["f(x)"], "o", label="Model 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("F(x) vs x Plot")
plt.legend()
plt.savefig("practicum3_zeinabenton_prob1d_plot3.png")
plt.show()

x = model2["x"]
y = model2["f(x)"]
sigma = np.full(len(y), 0.5) #uncertainty, np.full creates an array of the same length as y

(af, bf, a_unc, b_unc, chisq, prob, covar, yfit) = \
L.linfit(y, x, y_unc=sigma)

print("intercept =", af, "+/-", a_unc)
print("slope =", bf, "+/-", b_unc)

#check if within 3 sigma of true values
a_true = 1.2 # true intercept
b_true = 3.2 # true slope
print(abs(af - a_true) < 3*a_unc)
print(abs(bf - b_true) < 3*b_unc)

print("chi-square =", chisq)
print("probability =", prob)

plt.figure(figsize=(6,6))
plt.plot(x, y, "o", label="data")
plt.plot(x, yfit, label="fit")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("F(x) vs x Plot of Linear Fit to Model 2")
plt.legend()
plt.savefig("practicum3_zeinabenton_prob1d_plot4.png")
plt.show()


coeffs = np.polyfit(x, y, 2)
a = coeffs[0]
b = coeffs[1]
c = coeffs[2]
xfit = np.linspace(x.min(), x.max(), 1000)
yfit_quad = np.polyval(coeffs, xfit)
plt.figure(figsize=(6,6))
plt.plot(x, y, "o", label="data")
plt.plot(xfit, yfit_quad, label="quadratic fit")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("F(x) vs x Plot of Quadratic Fit to Model 2")
plt.savefig("practicum3_zeinabenton_prob1d_plot5.png")
plt.legend()
plt.show()



#%%
print("Problem 2:")
#a
poisson_data = np.random.poisson(lam=10000, size=396) #randomly generate 396 Poisson-distributed numbers
uniform_data = np.random.uniform(0, 1e6, size=4)
array = np.concatenate((poisson_data, uniform_data))

arr_mean = np.mean(array)
arr_med = np.median(array)
print("Mean of array:", arr_mean)
print("Median of array:", arr_med)

#b
arr_std = np.std(array)
print("Std of array:", arr_std)

mask = array[np.abs(array - arr_med) < 5*arr_std]
print("Mean =", np.mean(mask))
print("Median =", np.median(mask))
print("Std Dev =", np.std(mask))

# %%
