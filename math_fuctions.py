import numpy as np

x = np.array([-3, -2, -1, 0, 1, 2, 3])

print x.sum()
print x.max()
print x.min()
print x.mean()
print x.std()
print()
#return index of maximum, minimum
print x.argmax()
print x.argmin()

print("--------------------------------------------------------")
#Indexing and Slicing
a = np.arange(13)**2
print a
print a[1:5]
print a[-4:]
print a[-6::-2]

b = np.arange(36)
b.resize(6, 6)
print b
print b[5, 5]
print b[3, 3:6]
print b[:3, :-1]
print b[-1, ::3]
print b[b > 18]
b[b > 18] = 20
print b

#Coppy array
c = b[:3, :3]
print c
c[:] = 0
print b

b_real_copy = b.copy()
b_real_copy[:] = -1
print (b_real_copy)
print b