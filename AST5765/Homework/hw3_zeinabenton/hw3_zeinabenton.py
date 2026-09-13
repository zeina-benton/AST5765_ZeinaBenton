#Zeina Benton
#Homework 3
#9/13/26

#%%
"""
2. (36 points total) Write a function called square that returns the square of its input
(which may be a scalar or an array of any dimension or numerical type).
"""
#2f
from hw3_zeinabenton_support_functions import square

answer = square(5)
print(answer)
# %%
import numpy as np
from hw3_zeinabenton_support_functions import square

answer1 = square(np.array([4, 59, 67]))
print(answer1)
# %%
