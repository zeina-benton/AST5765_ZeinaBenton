#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Zeina Benton, HW2, 9/3/26


# 2. (10 points) Without using loops write the necessary Python commands that:
# a) a1) Create an array of integers x from 0 to 1000 (up to and including 1000). How
# many elements do you need?
# a2) Print the datatype of the array and the array’s minimum and maximum.
# Remember to answer all questions raised in the assignment, such as “how many
# elements do you need?”.
# b) b1) Re-scale x to contain values from 0 to 2π. Don’t make a new array, re-scale
# the array of question 2a.
# b2) Print the minimum and maximum values of the new x array.
# c) Make an array y whose values are the sine of the values of x.
# d) Print the value of element 234 of y [Note the difference between the 234th
# element and element 234 in Python!].

# In[11]:


import numpy as np
import pandas as pd
import os
import math
import time


# In[12]:


#2a1

x = np.arange(0,1001)
print(x) #1001 elements are needed to included 1000.


# In[13]:


#2b

print(x.dtype)
print(np.min(x))
print(np.max(x))


# In[14]:


#2b1

x = (x - np.min(x)) / (np.max(x) - np.min(x)) * (2 * np.pi)
print(x)


# In[15]:


#2b2

print(np.min(x))
print(np.max(x))


# In[16]:


#2c

y = np.sin(x)
print(y)


# In[17]:


#2d

print(y[234])


# 3. (10 points total) Write the necessary Python commands that:
# a) (5 points) Plot y vs. x from problem 2c. Make the plot publication-ready using
# reasonable axis labels etc.
# b) (5 points) Save your plot as a PNG using the appropriate Python commands (no
# screenshots or window dumps from outside Python).

# In[18]:


#3a
import matplotlib.pyplot as plt

plt.figure( figsize = (8, 6) )
plt.plot( x, y, color = 'red' , linewidth = 3 )
plt.xlabel( 'x ', fontsize = 14 )
plt.ylabel( 'y', fontsize = 14 )




#3b

plt.savefig("hw2_question3b_plot.png")


# 4. (10 points total)
# a) (5 points)
# a1) Make a “ramp” array r with 101 evenly spaced elements going from -1 to +1.
# a2) “Clip”, or mask, the array so that any value greater than 0.5 is set to 0.5 and
# any value less than -0.5 is set to -0.5. There are different ways that you can do
# this with numpy, but remember, no loops!
# b) (5 points)
# b1) In the same plot, plot the original and clipped arrays. Your figure should look
# something like this
# b2) Use the appropriate python command to save the plot as a PDF. Name the
# PDF appropriately.

# In[ ]:


#4a1

r = np.linspace(-1, 1, 101)
print(r)


# In[ ]:


#4a2

r_clipped = np.clip(r, -0.5, 0.5) 
print(r_clipped)


# In[33]:


#4b1

plt.figure( figsize = (8, 6) )
plt.title('Clipped Ramp', fontsize = 16 )
plt.plot( r, linewidth = 3 )
plt.plot( r_clipped, color = 'orange' , linewidth = 3 )
plt.xlabel( 'x ', fontsize = 14 )
plt.ylabel( 'Y', fontsize = 14 )



#4b2

plt.savefig("hw2_question4b2_plot.pdf")


# 5. (10 points) Give the URLs of two web sites outside of UCF that provide free
# astronomical software that is written in Python. Write a paragraph about each package
# in your own words. Put the two paragraphs as an extended string (between sets of triple
# single-quotes) in your main homework file.

# In[35]:


#Question 5 is answered in also written in log.

'''  Skyfield is a python package that helps computing positions for stars, planets, satellites 
in orbit around Earth. To use in your code, you would load in your file (I.e. asp) and then simply put 
the planet (i.e. 'earth' and 'mars') and then earth.at(t).observe(mars) to get the position and it's
 coordinates. 
https://rhodesmill.org/skyfield/ '''


''' PyCBC is a python package designed for gravitational wave astronomy and analysis. The modules within 
allow for signal processing, filtering, and transforms that work best with LIGO or Virgo data. It was used
in the firest detection of graviational waves by LIGO.
https://pycbc.org/'''



# In[ ]:




