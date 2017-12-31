import pandas as pd
import numpy as np

df = pd.read_csv('cars.csv')

# print df.head()

# print df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
print df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)