s = [1, 2, 3, 4, 2, 5, 2]
x = 2
print(list(i for i, elem in enumerate(s) if elem == x))
