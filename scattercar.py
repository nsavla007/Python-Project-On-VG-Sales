import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("car.csv")
df.plot(kind='scatter',x='distance traveled',y='starting point')
plt.show()