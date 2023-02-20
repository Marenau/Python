def f(s, с):
    count_c = 0
    for i in range(0, len(s)):
        if s[i] == с:
            count_c += 1
    return count_c
 
 
def count_characters(s):
    n = len(s)
    dict = {}
    s = s.lower();
    for i in range(0, n):
        key = s[i]
        if not (key in dict):
            value = f(s, key)
            dict[key] = value
    return dict


print(f('Alalalalar', 'a'))
print(count_characters('Alalalalar'))