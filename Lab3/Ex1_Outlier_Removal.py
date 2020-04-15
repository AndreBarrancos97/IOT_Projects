import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#************************************Exercise 1************************************************
df = pd.read_csv('EURUSD_Daily_Ask_2018.12.31_2019.10.05v2.csv')

x = np.linspace(-10 , 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")
plt.show()
