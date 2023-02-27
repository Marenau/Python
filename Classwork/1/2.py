import math as m


def f(n):
    if n == 0:
        return 6
    elif n == 1:
        return 4
    return 1 / 45 * f(n - 2) ** 3 + m.cos(f(n - 1))


print(f(12))
print(f(2))
