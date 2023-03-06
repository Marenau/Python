def main(dict):
    sum = 0
    sum += dict.get('L4')
    sum = sum << 2
    sum += dict.get('L3')
    sum = sum << 10
    sum += dict.get('L2')
    sum = sum << 5
    sum += dict.get('L1')
    return sum

print(main({'L1': 13, 'L2': 785, 'L3': 3, 'L4': 0}))
print(main({'L1': 30, 'L2': 842, 'L3': 2, 'L4': 1}))
print(main({'L1': 10, 'L2': 953, 'L3': 0, 'L4': 0}))
print(main({'L1': 12, 'L2': 922, 'L3': 3, 'L4': 1}))