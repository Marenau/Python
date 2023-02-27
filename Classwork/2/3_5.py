s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(s[i] for i in range(len(s)) if i % 2 == 0))
