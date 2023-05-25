from copy import deepcopy
from collections import OrderedDict


def main(table1):
    table = deepcopy(table1)
    
    table = [[row[j] for j in range(len(row)) if j not in (0, 3)] for row in table]

    table = [row for row in table if any(row)]

    # Создаем словарь с примерами преобразования
    transformation_dict = {
        0: lambda x: x[0 : x.find('[at]')],
        1: lambda x: x.replace('.', '/'),
        2: lambda x: x[x.find(' ') + 1:] + ' ' + x[0:1] + '.'
    }

    # Применяем преобразования к ячейкам таблицы
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = transformation_dict[j](table[i][j])

    # Удаляем повторяющиеся строки, сохраняя порядок
    table = list(OrderedDict((tuple(row), row) for row in table).values())

    
    return table


print(main([
    [None, 'nocigin1[at]rambler.ru&Да', '02.04.22', None, 'А.А. Ночигин'],
    [None, 'nocigin1[at]rambler.ru&Да', '02.04.22', None, 'А.А. Ночигин'],
    [None, 'ziluk78[at]mail.ru&Да', '03.02.21', None, 'И.З. Цилук'],
    [None, None, None, None, None],
    [None, 'nocigin1[at]rambler.ru&Да', '02.04.22', None, 'А.А. Ночигин'],
    [None, 'cisigin44[at]rambler.ru&Да', '04.11.25', None, 'Н.Ц. Чисигин'],
]))

print(main([
    [None, 'zolemak50[at]yahoo.com&Нет', '00.07.01', None, 'А.Ч. Цолемяк'],
    [None, 'dorin67[at]mail.ru&Да	', '01.08.21', None, 'В.Ш. Дорин'],
    [None, 'zufesidi99[at]yandex.ru&Да', '01.04.05	', None, 'Г.Н. Цуфесиди'],
    [None, 'zufesidi99[at]yandex.ru&Да', '01.04.05	', None, 'Г.Н. Цуфесиди'],
    [None, 'zufesidi99[at]yandex.ru&Да', '01.04.05	', None, 'Г.Н. Цуфесиди'],
]))
