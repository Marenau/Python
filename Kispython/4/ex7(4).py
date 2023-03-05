def main(dict):
    sum = 0
    sum += dict.get('Q6')
    sum = (sum << 4) + dict.get('Q5')
    sum = (sum << 7) + dict.get('Q4')
    sum = (sum << 9) + dict.get('Q3')
    sum = (sum << 4) + dict.get('Q2')
    sum = (sum << 4) + dict.get('Q1')
    return sum

print(main({'Q1': 15, 'Q2': 2, 'Q3': 13, 'Q4': 50, 'Q5': 14, 'Q6': 23}))
print(main({'Q1': 0, 'Q2': 13, 'Q3': 140, 'Q4': 116, 'Q5': 3, 'Q6': 10}))
print(main({'Q1': 0, 'Q2': 15, 'Q3': 241, 'Q4': 15, 'Q5': 12, 'Q6': 24}))
print(main({'Q1': 3, 'Q2': 7, 'Q3': 387, 'Q4': 62, 'Q5': 14, 'Q6': 31}))