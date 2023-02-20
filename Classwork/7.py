import math as m


def f(y, z):
    n = len(y)
    h = 5
    result = 0
    for i in range(0, n):
        result += m.abs((y[i] - z[i]) ** h)
    return result ** (1 / h)


print(f"{f([1, 0.5, 1], [0.5, 2, 1]):.3e}")
