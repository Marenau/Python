from copy import deepcopy


def main(table1):
    
    def transpose(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    
    table = deepcopy(table1)
    table = [row for row in table if any(row)]

    transformation_dict = {
        0: lambda x: x[6:8] + '/'+ x[3:5] + '/'+ x[0:2],
        1: lambda x: x.replace('@', '[at]'),
        2: lambda x: 0 if x == 'нет' else 1
    }

    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = transformation_dict[j](table[i][j])

    return transpose(table)


print(main([
    [None, None, None],
    [None, None, None],
    ['10-08-03', 'rumonli23@yahoo.com', 'нет'],
    ['12-05-03', 'galij51@mail.ru', 'нет'],
    ['12-10-00', 'soranz67@mail.ru', 'да']
]))

print(main([
    [None, None, None],
    ['11-11-99', 'zoriran99@rambler.ru', 'нет'],
    ['18-03-03', 'zumazanz63@rambler.ru', 'да'],
    ['28-06-02', 'zacudov30@yahoo.com', 'нет'],
    [None, None, None],
    ['03-12-01', 'zunidi83@yandex.ru', 'нет']
]))
