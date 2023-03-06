def main(x):
    int_x = int(x, base=16)
    R1 = int_x & 0b1111
    int_x >>= 4
    R2 = int_x & 0b111111111
    int_x >>= 9
    R3 = int_x & 0b111
    int_x >>= 3
    R4 = int_x & 0b111
    int_x >>= 3
    R5 = int_x & 0b111111
    return [('R1', str(R1)),
            ('R2', str(R2)),
            ('R3', str(R3)),
            ('R4', str(R4)),
            ('R5', str(R5))]


print(main('0x6a9f6'))
print(main('0x2464d1'))
print(main('0x18ba48b'))
print(main('0xb077e5'))
