import datetime
import time

print time.time()
dtnow = datetime.datetime.fromtimestamp(time.time())
print dtnow

delta = datetime.timedelta(days = 100)
print delta

today = datetime.date.today()
print today
print today - delta
print today > today - delta