import math as m


def f(n, m):
    summ1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            summ1 += i // 1 - 76 * j
    summ1 *= 22

    summ2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            summ2 += (42 * j + 90 * j ** 4 - 8)

    summ2 /= 31

    return summ1 - summ2


print(f(88, 80))
print(f(21, 83))
