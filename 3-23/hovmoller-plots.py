import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np


data = Dataset("/Users/brownscholar/Desktop/copied_atlantic-w.nc")
w_array = data.variables['w'][:]
date = 0 #what formati do I need to reference time in?
timeslice = w_array[date,:,:,0]

#this stuff defines the colorspace (we can google colormaps to learn more if we want to)
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')


p = plt.pcolormesh(timeslice[2:-2,2:-2],cmap = newcmp)

plt.colorbar()
plt.xlabel("Longitude")# labels x axis
plt.ylabel("Latitude")# labels the y axis
plt.title("ColorMap")# labels the entire map
plt.scatter([],[], color = "blue", label = "going down")#lables legend
plt.scatter([],[], color = "red", label = "going up")#lables legend
plt.legend(bbox_to_anchor=[1.0,1.0])# create legend
#plt.xticks(np.arange(0,num_lon,10),lon[::10])
#plt.yticks(np.arange(0,num_lat,10),lat[::10])
plt.show()

# import data (atlantic-w.nc) into a variable
# cut a time slice using same method from density.py
# create plot with this time slice 