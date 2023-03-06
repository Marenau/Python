def main(x):
    int_x = int(x)
    C1 = int_x & 0b1111111
    int_x >>= 7
    C2 = int_x & 0b111
    int_x >>= 3
    C3 = int_x & 0b111111
    int_x >>= 6
    C4 = int_x & 0b1111
    sum = C2
    sum <<= 4
    sum += C4
    sum <<= 6
    sum += C3
    sum <<= 7
    sum += C1
    return str(sum)


print(main('743096'))
print(main('42860'))
print(main('742832'))
print(main('992703'))
