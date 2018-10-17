## Cool Visualistions ##
# Plots 3d graphs of planes of 2 dimensional
# functions


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import argparse

#################################################################################
ap = argparse.ArgumentParser(description = 'The bounds and function')
ap.add_argument('lowx',action = "store" , help = 'The lower bounds of x'
,type = float,default = 2)
ap.add_argument('hix',action = "store" , help = 'The upper bounds of x'
,type = float,default = 2)
ap.add_argument('lowy',action = "store" , help = 'The lower bounds of y'
,type = float,default = 2)
ap.add_argument('hiy',action = "store" , help = 'The upper bounds of y'
,type = float,default = 2)
ap.add_argument('lim',action = "store" , help = 'The Z limits'
,type = float,default = 2)
args = vars(ap.parse_args())
#################################################################################

## Taking the args ##

lx = args['lowx']
hx = args['hix']
ly = args['lowy']
hy = args['hiy']
m = args['lim']

## The plotting ##

fig = plt.figure()  ## Starting the figure call
ax = fig.gca(projection='3d')

# Make data
X = np.arange(lx, hx, 0.005)
Y = np.arange(ly, hy, 0.005)
X, Y = np.meshgrid(X, Y)
Z = X*np.sin(X*Y)  # Alter this to change f(x,y)

# Plot the surface, note change colour with cmap cm.COLOUR
surf = ax.plot_surface(X, Y, Z, cmap=cm.plasma,
                       linewidth=0, antialiased=False)

# Customize the z axis
ax.set_zlim(-m*np.amax(Z),m*np.amax(Z))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors and other cool things
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Visualisation of Double Integral Surface ')


plt.show()
