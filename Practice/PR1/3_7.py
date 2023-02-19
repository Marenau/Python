def columnMultiplication(num1, num2):
    def toBin(num):
        # Выполнение проверки на 0
        if (num == 0):
            return '0'
        # Переменная, хранящая переведённое число
        result = ''
        # Цикл перевода числа
        while num > 0:
            # Добавление остатка от деления
            result += str(num % 2)
            # Сохранение целой части от деления
            num //= 2
        return result[::-1]

    def binSumm(num1, num2):
        # Находим максимальную длину двоичных чисел a и b
        maxLen = max(len(num1), len(num2))
        # Дополняем двоичные числа до одинаковой длины нулями
        num1 = num1.zfill(maxLen)
        num2 = num2.zfill(maxLen)
        result = ''
        flag = 0
        # Перебираем каждый бит с конца к началу
        for i in range(maxLen - 1, -1, -1):
            # Сложение с переполнением
            if num1[i] == '1' and num2[i] == '1':
                result = ('1' if flag else '0') + result
                flag = 1
            # Сложение даёт 0
            elif num1[i] == '0' and num2[i] == '0':
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
    binA = toBin(num1)
    binB = toBin(num2)
    # Переменная для двоичной суммы
    summ = ''
    # Цикл по бинарным цифрам числа b
    for i in range(0, len(binB)):
        # Получение последней цифры числа b
        m = int(binB[len(binB) - 1], base=2)
        # Выполнение двоичного сложения с учётом сдвига
        summ = binSumm(summ, str((int(binA) * m) * (10 ** i)))
        # Удаление последней цифры числа
        binB = binB[:-1]
    return int(summ, base=2)

print(columnMultiplication(2, 6))