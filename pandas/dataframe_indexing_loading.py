import pandas as pd
import numpy as np

p1 = pd.Series({
    'Name': 'js',
    'Item Purchased': 'Cat Food',
    'Cost': 22500
})

p2 = pd.Series({
    'Name': 'ds',
    'Item Purchased': 'Water',
    'Cost': 1500
})

p3 = pd.Series({
    'Name': 'ej',
    'Item Purchased': 'sasimi',
    'Cost': 30000
})

df = pd.DataFrame([p1, p2, p3], index=['s1', 's2', 's3'])

costs = df['Cost']
print costs

costs+=2000
print costs

df = pd.read_csv('olympics.csv')
print df.head()
print("------------------------------------------------------")
df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
print df.head()
print df.columns
print("------------------------------------------------------")

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)

print df.head()

print df['Gold'] > 0

gold = df.where(df['Gold'] > 0)
print gold.head()
print("------------------------------------------------------")
print gold['Gold'].count()
print df['Gold'].count()

gold = gold.dropna()
print gold.head()
print len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])
print df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]
print("------------------------------------------------------")
print("------------------------------------------------------")
#Indexing Dataframes
df['country'] = df.index
df = df.set_index('Gold')
print df.head()

df = df.reset_index()
print df.head()

df = pd.read_csv('census.csv')
print df.head()
print df['SUMLEV'].unique()
df=df[df['SUMLEV'] == 50]
print df.head()


columns_to_keep = ['STNAME',
                  'CTYNAME',
                  'REGION',
                  'DIVISION',
                  'STATE']
df = df[columns_to_keep]
print df.head()

df = df.set_index(['STNAME', 'CTYNAME'])
print df.head()
print df.loc['Alabama', 'Blount County']

print df.loc[[('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')]]

#Missing values
df = pd.read_csv('log.csv')
print df
df = df.set_index('time')
df = df.sort_index()
print df
df = df.reset_index()
df = df.set_index(['time', 'user'])
print df
df = df.fillna(method='ffill')
print df.head()