import numpy as np

list = [1, 2, 3]
y = np.array(list)

print y.shape

m = np.array([[1, 2, 3], [3, 4, 5]])
print m.shape

n = np.arange(0, 30, 2)
print n
n = n.reshape(3, 5)
print n

o = np.linspace(0, 4, 9)
print o

o.resize(3, 3)
print o

print np.zeros((3, 2))
print np.eye(5)

print np.diag(y)

print np.array([1, 2, 3] * 3)
print np.repeat([1, 2, 3], 3)

i = np.ones([2, 3], int)
print i

print np.vstack([i, 2*i])
print np.hstack([i, 2*i])
