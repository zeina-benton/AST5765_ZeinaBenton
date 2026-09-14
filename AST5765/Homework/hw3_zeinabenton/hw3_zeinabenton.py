#Zeina Benton
#Homework 3
#9/13/26

#%%
"""
2. (36 points total) Write a function called square that returns the square of its input
(which may be a scalar or an array of any dimension or numerical type).
"""
#2f
from hw3_zeinabenton_support_functions import square, squareplot

answer = square(5)
print(answer)

import numpy as np
from hw3_zeinabenton_support_functions import square

answer1 = square(np.array([4, 59, 67]))
print(answer1)

# %%
#2h
test_square_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(square(test_square_1))

# %%
#2i
test_square_2 = np.arange(25, dtype=float).reshape(5, 5)
print(square(test_square_2))


# %%
squareplot(1, 7, 5, saveplot='hw3_zeinabenton_squareplot.pdf')

# %%
