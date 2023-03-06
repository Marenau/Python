def main(x):
    sum = 0
    sum += int(x[2])
    sum = sum << 9
    sum = sum << 9
    sum += int(x[1])
    sum = sum << 7
    sum += int(x[0])
    return sum

print(main(('15', '308', '5')))
print(main(('116', '95', '22')))
print(main(('18', '448', '0')))
print(main(('88', '347', '12')))