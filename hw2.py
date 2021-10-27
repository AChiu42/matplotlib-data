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
plt.savefig('Amount_of_Rainfall_per_year_in_contiguous_united_states')
plt.show()


# Plots for US and China GDP
# GDP of US
with open('NY.GDP.MKTP.json', encoding = 'ascii') as f:
    US_GDP = json.loads(f.read())

US_x = []
for year_US in range(2020, 1959, -1):
    US_x.append(year_US)

US_y=[]
for dict in US_GDP[1]:
    US_y.append(dict['value'])

# GDP of China
with open('NY.GDP.MKTP.China.json', encoding = 'ascii') as f:
    China_GDP = json.loads(f.read())

China_x=[]
for year_China in range(2020, 1959, -1):
    China_x.append(year_China)

China_y=[]
for dict in China_GDP[1]:
    China_y.append(dict['value'])

# Scatter plot with both data sets
plt.xlabel('Years')
plt.ylabel('GDP (Ten Trillions)')
plt.title('GDP of United States vs China Time')
plt.scatter(US_x, US_y, label = 'GDP of US')
plt.scatter(China_x, China_y, label = 'GDP of China')
plt.legend()
plt.savefig('US_vs_China_GDP.png')
plt.show() 
