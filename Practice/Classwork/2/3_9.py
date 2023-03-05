from itertools import groupby


string = 'ABBCCCDEF'
print(''.join([f'{char}{len(list(group))}' for char, group in groupby(string)]) )
