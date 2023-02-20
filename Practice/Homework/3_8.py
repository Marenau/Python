def columnMultiplicationPow(num1, num2):
    # Функция перевода в двоичную СС
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

    # Фукнкция двоичной суммы
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

    # Переводим число в двоичный формат
    constNum1 = toBin(num1)
    # Переменная для двоичной суммы
    summ = constNum1
    # Цикл возведения в степень
    for i in range(1, num2):
        # Сохранение предыдущей суммы
        binA = summ
        # Обнуление текущей суммы
        summ = ''
        # Цикл по бинарным цифрам числа b
        for j in range(0, len(constNum1)):
            # Получение последней цифры числа b
            m = int(constNum1[len(constNum1) - 1], base=2)
            # Выполнение двоичного сложения с учётом сдвига
            summ = binSumm(summ, str((int(binA) * m) * (10 ** j)))
            # Удаление последней цифры числа
            constNum1 = constNum1[:-1]
        constNum1 = toBin(num1)
    return int(summ, base=2)


print(columnMultiplicationPow(6, 3))