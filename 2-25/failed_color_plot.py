import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

w_file = '/Users/brownscholar/desktop/GITHUB2021/ocean-motion-2021/2-25/ss1a2ww.gr' # fix this
w = open(w_file, "r")

#open netcdf file
original_data = Dataset("/Users/brownscholar/Desktop/n-atlantic-2018.nc"

#get latitude and longitude from netcdf file: 
# here:
lat = original_data.variables[]
lon = original_data.variables[]

num_lat = 158
num_lon = 122
levels = 1

# make empty numpy array of shape lat, lon depth shape for storing w:
w_values = np.zeros((num_lat, num_lon, levels))

# use a loop to read w_file into the variable 
#(skip first two lines of the file)
w.readline()
w.readline()
for i in range(0, levels):
	for j in range(0, num_lat):


#this stuff defines the colorspace (we can google colormaps to learn more if we want to)
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')




#now use the following function to plot your data:
#function to make colorplot is:
# p = plt.pcolormesh(V,cmap = newcmp), where V is the numpy array with the data

# you can use these to add the x and y ticks to your plot:
# I am happy to talk to you about why this works
#plt.xticks(np.arange(0,num_lon,10),lon[::10])
#plt.yticks(np.arange(0,num_lat,10),lat[::10])


