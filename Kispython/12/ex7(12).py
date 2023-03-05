def main(string):
    int_string = int(string, base=16)
    return (int_string & 0b11111111,
            (int_string >> 8) & 0b111111,
            (int_string >> 14) & 0b111)

print(main('0x1bad8'))
print(main('0x5572'))
print(main('0x132c8'))
print(main('0x10d8f'))