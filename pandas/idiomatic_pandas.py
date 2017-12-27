import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
# print df.head()

# print (df.where(df['SUMLEV']==50)
#         .dropna()
#         .set_index(['STNAME', 'CTYNAME'])
#         .rename(columns={'ESTIMATESBASE2010': 'Estimates base 2010'}))

df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

# print df

def max_min(row):
    data = row[[
        'POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015'
        ]]
    return pd.Series({'max': np.max(data), 'min': np.min(data)})    

print df.apply(max_min, axis=1)