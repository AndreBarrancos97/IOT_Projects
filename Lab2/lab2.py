import numpy as np
import pandas as pd

#************************************Exercise 1************************************************
df = pd.read_csv('AAPL_yah.csv')

df1 = df.sort_values(by=['Close'])

df1.to_csv('ChangedData.csv')

df1.to_csv('ChangedData1.csv', decimal=',', sep=';', index= False)

#***********************************************************************************************

#************************************Exercise 2************************************************
import time
start_time = time.process_time()

df['newCol'] = df['Volume'].cumsum()
df.to_csv('NewData.csv')
print("time used in cumsum -->", time.process_time() - start_time, "seconds")

#***********************************************************************************************

#************************************Exercise 3************************************************
a = np.arange(10)
print(a)
#a = array ([0,1,2,3,4,5,6,7,8,9])

b = np.where(a < 5, a, 10*a)
print(b)
#array([0,1,2,3,4,50,60,70,80,90])

df['signal'] = np.where(df['Close'] > df['Open'], 1.0, 0.0)
df.to_csv('NewData.csv')

#***********************************************************************************************
import matplotlib.pyplot as plt

x = np.linspace(-10 , 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")
plt.show()

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()