def main(table):
    table = [[row[j] for j in range(len(row)) if j not in (3, 4, 5)] for row in
             table]

    table = [row for row in table if any(row)]

    # Создаем словарь с примерами преобразования
    transformation_dict = {
        0: lambda x: x[8:10] + '-' + x[3:5] + '-' + x[0:2],
        1: lambda x: 'Y' if x == 'true' else 'N',
        2: lambda x: '(' + x[2:5] + ') ' + x[5:8] + '-' + x[8:12]
    }

    # Применяем преобразования к ячейкам таблицы
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = transformation_dict[j](table[i][j])

    return table


print(main([
    ["23-04-2002", "true", "+76760109239", None, None, "+76760109239"],
    ["16-12-1999", "true", "+73762813721", None, None, "+73762813721"],
    [None, None, None, None, None, None],
    ["20-04-2003", "true", "+71441271199", None, None, "+71441271199"],
    ["20-11-2001", "true", "+73315187431", None, None, "+73315187431"],
]))

print(main([
    ["03-02-2004", "false", "+77830599290", None, None, "+77830599290"],
    ["05-01-2000", "true", "+73921387074", None, None, "+73921387074"],
    [None, None, None, None, None, None],
    ["15-07-2000", "true", "+74493522473", None, None, "+74493522473"],
]))
