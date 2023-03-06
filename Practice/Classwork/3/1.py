def main(x):
    sum = 0
    sum +=int(x.get('z6'))
    sum <<= 6
    sum += int(x.get('z5'))
    sum <<= 2
    sum <<= 6
    sum += int(x.get('z3'))
    sum <<= 6
    sum += int(x.get('z2'))
    sum <<= 3
    sum += int(x.get('z1'))
    return hex(sum)


print(main({'z1': '3', 'z2': '2', 'z3': '11', 'z5': '32', 'z6': '525'}))
print(main({'z1': '5', 'z2': '55', 'z3': '2', 'z5': '53', 'z6': '1016'}))
print(main({'z1': '3', 'z2': '46', 'z3': '43', 'z5': '29', 'z6': '387'}))
print(main({'z1': '3', 'z2': '47', 'z3': '51', 'z5': '40', 'z6': '550'}))
