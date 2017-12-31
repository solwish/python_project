import pandas as pd
import numpy as np

df = pd.DataFrame(['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D'])
df.rename(columns={0: 'Grades'}, inplace=True)
# print df

print df['Grades'].astype('category').head()
grades = df['Grades'].astype('category',
                            categories=['D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+'],
                            ordered=True)
print grades

print grades > 'B'

df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
print pd.cut(df['avg'], 10)
