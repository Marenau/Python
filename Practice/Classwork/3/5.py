def main(x):
    int_x = int(x)
    S1 = int_x & 0b111
    S2 = (int_x >> 3) & 0b1111
    S4 = (int_x >> 17) & 0b1111111111
    S5 = (int_x >> 27) & 0b1111111111
    sum = S2
    sum <<= 10
    sum += S5
    sum <<= 3
    sum += S1
    sum <<= 20
    sum += S4
    return hex(sum)


print(main('239948252'))
print(main('128390864606'))
print(main('51700518902'))
print(main('94668019137'))