import pandas as pd
import numpy as np

p1 = pd.Series({
    'Name': 'js',
    'Item Purchased': 'Cat Food',
    'Cost': '22500'
})

p2 = pd.Series({
    'Name': 'ds',
    'Item Purchased': 'Water',
    'Cost': '1500'
})

p3 = pd.Series({
    'Name': 'ej',
    'Item Purchased': 'sasimi',
    'Cost': '30000'
})

df = pd.DataFrame([p1, p2, p3], index=['s1', 's2', 's3'])
print df.head()

# print pd.Series(p1).append(p2)

print "--------------------------------------------------"

print df.loc['s2']
# print df.iloc[1]
print df.loc['s3', 'Cost']
print "--------------------------------------------------"
print df.T

print "--------------------------------------------------"
print df.loc[:,['Name', 'Cost']]

print df.drop('s1')
print df

copy_df = df.copy()
copy_df = copy_df.drop('s1')
print copy_df

print "--------------------------------------------------"

del copy_df['Cost']
print copy_df

df['Location'] = None
print df