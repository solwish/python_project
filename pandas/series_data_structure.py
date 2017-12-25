import pandas as pd
import numpy as np

animals = ['Dog', 'Cat', 'Rabbit']
print pd.Series(animals)

print np.nan == None
print np.nan == np.nan
print np.isnan(np.nan)

sports = {
    'Dumo' : 'Japan',
    'Taeckgen' : 'Korea'
}

p = pd.Series(sports)
print p
print p.index

p = pd.Series(['A', 'B', 'C'], index=['D', 'E', 'F'])
print p

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print s