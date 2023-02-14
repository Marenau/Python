def columnMultiplication(a, b):
    def toBin(a):
        # Выполнение проверки на 0
        if (a == 0):
            return '0'
        # Переменная, хранящая переведённое число
        result = ''
        # Цикл перевода числа
        while a > 0:
            # Добавление остатка от деления
            result += str(a % 2)
            # Сохранение целой части от деления
            a //= 2
        return result[::-1]


    def binSumm(a, b):
        # Находим максимальную длину двоичных чисел a и b
        maxLen = max(len(a), len(b))
        # Дополняем двоичные числа до одинаковой длины нулями
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        result = ''
        flag = 0
        # Перебираем каждый бит с конца к началу
        for i in range(maxLen - 1, -1, -1):
            # Сложение с переполнением
            if a[i] == '1' and b[i] == '1':
                result = ('1' if flag else '0') + result
                flag = 1
            # Сложение даёт 0
            elif a[i] == '0' and b[i] == '0':
                result = ('1' if flag else '0') + result
                flag = 0
            # Сложение без переполнения
            else:
                result = ('0' if flag else '1') + result
        # Если есть переполнение, то добавляем его в начало
        if flag:
            result = '1' + result
        return result
    
    # Переводим числа в двоичный формат
    binA = toBin(a)
    binB = toBin(b)
    # Переменная для двоичной суммы
    summ = ''
    # Цикл по юинарным цифрам числа b
    for i in range(0, len(binB)):
        # Получение последней цифры числа b
        m = int( binB[ len(binB) - 1 ], base = 2 )
        # Выполнение двоичного сложения с учётом сдвига
        summ = binSumm(summ, str( (int(binA) * m) * (10 ** i) ) )
        # Удаление последней цифры числа
        binB = binB[:-1]
    return int(summ, base = 2)
    
print(columnMultiplication(2, 6))