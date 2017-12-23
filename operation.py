import numpy as np

a = np.array([1, 2, 3])
print a
b = np.array([4, 5, 6])
print b
print a.dot(b)
c = np.array([b, b**2])
print(len(c))
print c
print c.shape

print c.T
print c.dtype
c = c.astype('f')
print c.dtype