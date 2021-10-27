import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os
import numpy as np


with open('rainfall.json', encoding = 'ascii') as f:
    rainfall = json.loads(f.read())


years = []

for key in rainfall['data'].keys():
    # if int(key) > 1984 and int(key) < 2011:
        years.append(key)
        
rain = []
for key in rainfall['data'].keys():
    rain.append(rainfall['data'][key]['value'])

print('years = ', years)

print('rain = ', rain)


plt.xlabel('Years Since 1895')
plt.ylabel('Inches of Rain')
plt.title('Rainfall in a Year in the Contiguous United States')
plt.plot(years, rain, label = 'rain in a year')
plt.tick_params(axis = 'x', rotation = 45, direction = 'in')
plt.tick_params(axis = 'y', rotation = 45, direction = 'in')
plt.xscale('linear')
plt.Axes
plt.xlim(0, 120)
plt.ylim(20, 40)
plt.xticks(np.arange(0, 120, 5), fontsize = 7, color = 'blue')
plt.yticks(np.arange(20, 40, 2), fontsize = 7, color = 'blue')
plt.show()
