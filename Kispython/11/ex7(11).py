def main(dict):
    sum = 0
    sum += dict[3][1]
    sum = sum << 8
    sum += dict[2][1]
    sum = sum << 6
    sum = sum << 3
    sum += dict[1][1]
    sum = sum << 7
    sum += dict[0][1]
    return hex(sum)

print(main([('T1', 110), ('T2', 6), ('T4', 207), ('T5', 859)]))
print(main([('T1', 100), ('T2', 3), ('T4', 128), ('T5', 665)]))
print(main([('T1', 118), ('T2', 7), ('T4', 43), ('T5', 867)]))
print(main([('T1', 46), ('T2', 4), ('T4', 84), ('T5', 23)]))