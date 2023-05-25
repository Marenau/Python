def main(string):
    int_string = int(string)
    B1 = int_string & 0b111111
    int_string = int_string >> 6
    B2 = int_string & 0b1111111
    int_string = int_string >> 7
    B3 = int_string & 0b111111111
    int_string = int_string >> 9
    B4 = int_string & 0b111111
    int_string = int_string >> 6
    B5 = int_string & 0b1111111
    int_string = int_string >> 7
    B6 = int_string & 0b11
    summ = 0
    summ += B1
    summ = summ << 9
    summ += B3
    summ = summ << 7
    summ += B2
    summ = summ << 7
    summ += B5
    summ = summ << 6
    summ += B4
    summ = summ << 2
    summ += B6
    return summ

print(main('103799041609'))
print(main('43394788641'))
print(main('70440722370'))
print(main('117250758461'))