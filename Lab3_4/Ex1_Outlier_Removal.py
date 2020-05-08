
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import datetime as dt
from itertools import filterfalse

# Look to the path of your current working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
#************************************Exercise 1************************************************
def outlier_treatment(datacolumn):
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn , [25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range,upper_range

x = []
y = []

df = pd.read_csv(working_directory + '/EURUSD_Daily_Ask_2018.12.31_2019.10.05v2.csv', delimiter=';')

list_of_rows = [list(row) for row in df.values]

for row in list_of_rows:
    timestamp = pd.to_datetime(row[0])
    x.append(int(time.mktime(timestamp.timetuple()))) 
    y.append(float(row[1].replace(',','.')))

#print(df['Time (UTC)'].values)
#x = np.linspace(-10 , 10, 100)
#y = np.sin(x)
#plt.xticks(x, list_of_rows[0])
l,u = outlier_treatment(y)
print(l)
print(u)
print(len(y))
y_without_outlier = []
x_without_outlier = []
i=0

for item in y:
    if (y[i] < u) and (y[i] > l):
        y_without_outlier.append(item)
        x_without_outlier.append(x[i])
    i = i + 1



print(y_without_outlier)
print(x_without_outlier)
plt.plot(x_without_outlier,y_without_outlier, marker="x")
plt.show()

