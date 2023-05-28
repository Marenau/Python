# Салман

def main(x):
    summ = 0
    summ += int(x[3][1])
    summ <<= 9
    summ += int(x[2][1])
    summ <<= 1
    summ += int(x[1][1])
    summ <<= 7
    summ += int(x[0][1])
    return str(hex(summ))
    
print(main([
    ('J1', '42'),
    ('J2', '0'),
    ('J3', '423'),
    ('J4', '352')
]))

print(main([
    ('J1', '55'),
    ('J2', '1'),
    ('J3', '304'),
    ('J4', '40')
]))

print(main([
    ('J1', '10'),
    ('J2', '1'),
    ('J3', '440'),
    ('J4', '356')
]))

print(main([
    ('J1', '92'),
    ('J2', '0'),
    ('J3', '312'),
    ('J4', '37')
]))