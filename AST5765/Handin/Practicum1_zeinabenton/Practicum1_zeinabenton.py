#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#1a and 1c (no loop)

array = np.zeros((300, 200), dtype = np.float64) + np.arange(200)


# In[3]:


#1b (loop)

for x in range(300):
    for y in range(200):
        array [x,y] = y



# In[4]:


#1d

plt.imshow(array, cmap = 'gray')
plt.gca().invert_yaxis()


# In[5]:


#1e

rand_x = np.random.randint(0, 300, size=5)
rand_y = np.random.randint(0, 200, size=5)

values = array[rand_x, rand_y]
print("Output:" , values)

rand_x1 = np.random.randint(0, 300, size=5)
rand_y1 = np.random.randint(0, 200, size=5)

values1 = array[rand_x1, rand_y1]
print("Output:" , values1)


# In[6]:


#2 Done in log.


# In[10]:


#3
import astropy.io.fits as fits

im = fits.getdata('m42_40min_ir.zip') 
plt.imshow(im, cmap='gray', origin='lower')

plt.xlabel('X pixel')
plt.ylabel('Y pixel')
plt.title('m42 Image - Zeina Benton')

plt.savefig('Practicum1_zeinbenton_problem3_m42figure.png')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




