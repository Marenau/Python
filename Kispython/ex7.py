def main(string):
    int_string = int(string)
    return [('Q1', str(int_string & 0b11111111)),
            ('Q2', str((int_string >> 8) & 0b111)),
            ('Q3', str((int_string >> 11) & 0b1111111111)),
            ('Q4', str((int_string >> 21) & 0b1111))]

print(main('21694745'))
print(main('1369661'))
print(main('14135379'))
print(main('19278281'))