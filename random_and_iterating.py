import numpy as np

t = np.random.randint(0, 20, (4, 4))
print t

print("----------------------------------")
for row in t:
    print row
    
print("----------------------------------")
for i in range(len(t)):
    print(t[i])
    
print("----------------------------------")
for i, j in enumerate(t):
    print('row', i, 'is', j)

t2 = t**2

for i, j in zip(t, t2):
    print(i,'+',j,'=',i+j)