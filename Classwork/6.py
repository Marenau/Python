import math as m


def f(y, z):
    sixth_ans = 0
    n = len(y)
    for i in range(0, n):
        sixth_ans += (y[i] - z[i]) ** 2
    return sixth_ans


print(f([1, 0.5, 1], [0.5, 2, 1]))