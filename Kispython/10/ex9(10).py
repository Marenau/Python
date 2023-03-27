def main(table):
    empty_cells = [(i, j) for i in range(len(table)) for j in
                   range(len(table[0])) if table[i][j] is None]
    for i, j in reversed(empty_cells):
        del table[i][j]

    # Создаем словарь с примерами преобразования
    transformation_dict = {
        0: lambda x: x[6:8] + '-' + x[3:5] + '-' + x[:2],
        1: lambda x: x.replace(',', '')[:-2],
        2: lambda x: '+7 (' + x[2:5] + ') ' + x[5:8] + '-' + x[8:10] + '-' + x[
            10:12]
    }

    # Применяем преобразования к ячейкам таблицы
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = transformation_dict[j](table[i][j])

    # Сортируем таблицу по столбцу №3
    table.sort(key=lambda x: x[2])

    return table


print(main([
    ['04-02-01', 'Бозко, С.Ш.', '+72747864681'],
    ['04-12-10', 'Кашачин, О.Е.', '+74949436264'],
    ['02-10-16', 'Кеско, Э.Е.', '+74884207642'],
    ['03-04-08', 'Чизакий, Д.Р.', '+78945971456']
]))

print(main([
    ['04-04-19', 'Тицак, Д.М.', '+76494657375'],
    ['01-05-07', 'Мерофли, Д.Б.', '+75464350516'],
    ['03-01-10', 'Рогузян, О.И.', '+75282245005'],
]))
