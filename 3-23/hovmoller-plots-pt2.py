import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np
import datetime as td

data = Dataset("/Users/brownscholar/Desktop/atlantic-data.nc")
w_array = data.variables['w'][:]
lat=153
latitude = data.variables['latitude'][lat]
print(latitude)
timeslice = w_array[:,lat,:,0]

rotated_timeslice = np.rot90(timeslice)

top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')

#Y-AXIS
longitude_values = [312.125, 312.375, 312.625, 312.875, 313.125, 313.375, 313.625, 313.875, 314.125, 314.375, 314.625, 314.875, 315.125, 315.375, 315.625, 315.875, 316.125, 316.375, 316.625, 316.875, 317.125, 317.375, 317.625,  317.875, 318.125, 318.375, 318.625, 318.875, 319.125, 319.375, 319.625, 319.875, 320.125, 320.375, 320.625, 320.875, 321.125, 321.375, 321.625,  321.875, 322.125, 322.375, 322.625, 322.875, 323.125, 323.375, 323.625, 323.875, 324.125, 324.375, 324.625, 324.875, 325.125, 325.375, 325.625, 325.875, 326.125, 326.375, 326.625, 326.875, 327.125, 327.375, 327.625, 327.875, 328.125, 328.375, 328.625, 328.875, 329.125, 329.375, 329.625, 329.875, 330.125, 330.375, 330.625, 330.875, 331.125, 331.375, 331.625, 331.875, 332.125, 332.375, 332.625, 332.875, 333.125, 333.375, 333.625, 333.875, 334.125, 334.375, 334.625, 334.875, 335.125, 335.375, 335.625, 335.875, 336.125, 336.375, 336.625, 336.875, 337.125, 337.375, 337.625, 337.875, 338.125, 338.375, 338.625, 338.875, 339.125, 339.375, 339.625, 339.875, 340.125, 340.375, 340.625, 340.875, 341.125, 341.375]

for i in range(len(longitude_values)):
    longitude_values[i] = longitude_values[i]-360
print(longitude_values)

#X-AXIS
startdate = td.date(1950,1,1)
oritime = data.variables['time'][:]
yearlist = []
for i in (range(0,len(oritime),52)):
    yearss = startdate + td.timedelta(hours = int(oritime[i]))
    yearlist.append(yearss.year)
print(yearlist)

#PLOTTING
fig, ax = plt.subplots()
plt.pcolormesh(rotated_timeslice,cmap = newcmp, vmax=1, vmin=-1)
plt.title("Hovmoller Diagrams at Latitude "+str(latitude)+"•N")
plt.colorbar()
plt.xlabel("Years")# labels x axis
plt.ylabel("Longitude (•W)")# labels the y axis
plt.scatter([],[], color = "blue", label = "going down")#lables legend
plt.scatter([],[], color = "red", label = "going up")#lables legend
plt.legend(bbox_to_anchor=[1.0,1.0])# create legend
ax.set_xticks(np.arange(0,1355,52))
ax.set_xticklabels(yearlist, rotation = 90, fontsize=7)
ax.set_yticks(np.arange(0, 118 , 20 ))
ax.set_yticklabels(longitude_values[0::20])

plt.savefig("/Users/brownscholar/desktop/Hovmoller_plots")

plt.show()
