from copy import deepcopy
from collections import OrderedDict


def main(table1):
    def transpose(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    table = deepcopy(table1)
    
    table = [row for row in table if any(row)]
    
    for row in table:
        column_value = row[0]
        split_values = column_value.split('#')
        row[0] = split_values[1]
        row.insert(1, split_values[0])


    # Создаем словарь с примерами преобразования
    transformation_dict = {
        0: lambda x: x[:x.find('[at]')],
        1: lambda x: x.replace('-', '.'),
        2: lambda x: x[x.find(' ') + 1:] + ' ' + x[0:1] + '.'
    }

    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = transformation_dict[j](table[i][j])

    table = list(OrderedDict((tuple(row), row) for row in table).values())
    
    return transpose(table)


print(main([
    ['07-10-02#gadazli27[at]mail.ru', 'И.И. Гадацли'],
    ['08-05-01#votorli76[at]yahoo.com', 'И.У. Воторли'],
    ['08-05-01#votorli76[at]yahoo.com', 'И.У. Воторли'],
    ['01-02-01#sovokanz30[at]yahoo.com	', 'В.Д. Совокянц'],
    [None, None],
    ['08-02-00#facak65[at]yandex.ru', 'А.Ф. Фачак'],
    ['08-05-01#votorli76[at]yahoo.com', 'И.У. Воторли'],
]))
