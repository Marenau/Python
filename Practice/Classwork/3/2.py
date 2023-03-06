def main(x):
    sum = 0
    sum += x[5]
    sum <<= 1
    sum += x[4]
    sum <<= 4
    sum += x[3]
    sum <<= 1
    sum += x[2]
    sum <<= 9
    sum += x[1]
    sum <<= 9
    sum += x[0]
    return sum


print(main((376, 159, 1, 0, 1, 21)))
print(main((130, 60, 1, 11, 1, 52)))
print(main((376, 444, 0, 14, 0, 33)))
print(main((119, 199, 1, 12, 0, 27)))
