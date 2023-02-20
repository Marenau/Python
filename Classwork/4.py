import math as m


def f(y, z):
    n = len(y)
    summ = 0
    for i in range(1, n + 1):
        summ += m.abs(y[i - 1] - z[i - 1])
    return summ


print(f([1,  0.5, 1], [0.5, 2, 1]))