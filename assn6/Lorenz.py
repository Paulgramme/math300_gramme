
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(x, y, z, a=10, b=28, c=2.667):
    xnew = a*(y - x)
    ynew = b*x - y - x*z   #equations
    znew = x*y - c*z
    return xnew, ynew, znew
dt = 0.01
stepcount = 1000
dx = np.empty((stepcount + 1,))
dy = np.empty((stepcount + 1,))    #clear
dz = np.empty((stepcount + 1,))
dx[0], dy[0], dz[0] = (1, 1, 1)
for i in range(stepcount):
    xnew, ynew, znew = lorenz(dx[i], dy[i], dz[i])
    dx[i + 1] = dx[i] + (xnew * dt)
    dy[i + 1] = dy[i] + (ynew * dt)             #derive
    dz[i + 1] = dz[i] + (znew * dt)
    
plt.plot(dy,dz)            #plot
plt.show()

