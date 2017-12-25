import pandas as pd
import numpy as np


di = {
    'A': 'D',
    'B': 'E',
    'C': 'F'
}
se = pd.Series(di)
print se

print se.iloc[2]
print se[2]

print se.loc['C']
print se['C']

d = {
    97: 'A',
    99: 'B',
    100: 'C'
}
si = pd.Series(d)
print si
# print s[0]  #error

s = pd.Series(np.random.randint(0, 1000, 10000))
print s.head

s += 2
print s.head

for label, value in s.iteritems():
    s.set_value(label, value+2)
print s.head()
c = se.append(si)
print c