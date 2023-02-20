import math as m


def f(y, z):
    n = len(y)
    maximum = y[0]
    for i in range(1, n + 1):
        local_dist = abs(y[i - 1] - z[i - 1])
        if maximum < local_dist:
            maximum = local_dist
    return maximum


print(f([1,  0.5, 1], [0.5, 2, 1]))