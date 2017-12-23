my_func = lambda a, b, c : a + b

print my_func(1, 2, 3)

list = []

for num in range(0, 1000):
    if num % 49 == 0:
        list.append(num)

print list

list = [num for num in range(0, 1000) if num % 49 == 0]
print list
