# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:32:08 2022

@author: Sangita 
"""
# Horizontal Bar Graph 

# importing libraries 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl

# Loading Superstore dataset. 
dataset = pd.read_csv("Superstore.csv", encoding='unicode_escape')
df = pd.DataFrame(dataset)
required = df[['Sub-Category', 'Sales']]

# Groupping Sub-Category based on total Sales in ascending order
final =required.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=True)

# Formatting the bar graph
visual = final.plot(kind="barh", color= 'green')
plt.title("Total Sales By Sub-Category 2014 to 2017")
plt.xlabel ("Total Sales")
visual.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))


###############################################

#Scatterplot 

#Importing libraries and Dataset 
import numpy as np 

data = np.genfromtxt('faithful.csv', delimiter=',', skip_header=1)
plt.figure()

plt.plot(data[:,1], data[:,2], '.b', label='Observations')
plt.xlabel('Eruption Duration (minutes)')
plt.ylabel('Time bewteen Eruptions (minutes)')
plt.ylim([0,100])


duration_mean = np.mean(data[:,1])
wait_mean = np.mean(data[:,2])

duration_std = np.mean(data[:,1])
wait_std = np.std(data[:,2])

plt.errorbar(duration_mean, wait_mean,fmt='xr', xerr=duration_std,
             yerr=wait_std, label="Descriptive Statistics")


coefs= np.polyfit(data[:,1], data[:,2], 1)
plot_x = np.array([1.5, 5.5])
plot_y =coefs[0]*plot_x + coefs[1]

plt.plot(plot_x, plot_y, ':r', label='Linear Regression')
plt.legend(loc='lower right')


##########################################################

#Bar graph 
#Importing libraries and Data Set 

import pandas as pd 
import matplotlib.pyplot as plt
dataset = pd.read_csv("Superstore.csv", encoding='unicode_escape')

bargraph = dataset.pivot_table(index='Region', columns=('Category'), values=('Sales'), aggfunc='sum').plot(kind='bar')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Total sales by Region and Category (2014-2017)')
plt.legend(bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)
print(bargraph)







