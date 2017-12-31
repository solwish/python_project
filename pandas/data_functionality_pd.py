import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#timestamp
print pd.Timestamp('12/31/2017 12:49PM')

#period
print pd.Period('12/2017')
print pd.Period('12/31/2017')

#datetime index
time1 = pd.Series(list('rfc'), [pd.Timestamp('2017-12-31'),
                                pd.Timestamp('2018-01-01'),
                                pd.Timestamp('2018-01-02')])
print time1
print type(time1.index)

#period index
time2 = pd.Series(list('def'), [pd.Period('2017-12'), pd.Period('2018-01'), pd.Period('2018-02')])
print time2
print type(time2.index)

#converting to datetime
date1 = ['2 June 2015', 'Aug 29, 2016', '2017-06-26', '7/12/18']
time3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=date1, columns=list('ab'))
print time3

time3.index = pd.to_datetime(time3.index)
print time3

print pd.to_datetime('11.7.17', dayfirst=True)

#time deltas

print pd.Timestamp('12/31/2017')-pd.Timestamp('1/2/2018')
print pd.Timestamp('12/31/2017 1:55PM') + pd.Timedelta('30D 3H')

#working with dates in a dataframe
dates = pd.date_range('12-30-2017', periods=9, freq='2w-SUN')
print dates

df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 200 + np.random.randint(-5, 10, 9)}, index=dates)
print df
print df.index.weekday_name
print df.diff()
print df.resample('M').mean()
print df['2018']
print df['2018-02']
print df['2018-02':]
print df.asfreq('W', method='ffill')

# print df.plot()