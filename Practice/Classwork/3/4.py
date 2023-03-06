def main(x):
    int_x = int(x, base=16)
    N1 = int_x & 0b111111
    int_x >>= 6
    N2 = int_x & 0b111111
    int_x >>= 6
    N3 = int_x & 0b1111111
    int_x >>= 7
    N4 = int_x & 0b11
    int_x >>= 2
    N5 = int_x & 0b111
    return [{'N1', N1},
            {'N2', N2},
            {'N3', N3},
            {'N4', N4},
            {'N5', N5}]


print(main('0xb9a562'))
print(main('0x85c1a5'))
print(main('0xe3fb96'))
print(main('0x2909e9'))