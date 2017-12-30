import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
# print df


# for state in df['STNAME'].unique():
#     avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
#     # print('Counties in state ' + state + ' have an average population of ' + str(avg))
    
    
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    # print('Counties in state ' + group + ' have an average population of ' + str(avg))
    
# print df.head()

df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

# for group, frame in df.groupby(fun):
#     print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')



df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

# print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
# print(type(df.groupby(level=0)['POPESTIMATE2010']))

# print (df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
#     .agg({'avg': np.average, 'sum': np.sum}))

# print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
#         .agg({'avg': np.average, 'sum': np.sum}))
    
print (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
        .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))    