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
        m = int( binB[ len(binB) - 1 ], base = 2 )
        # Выполнение двоичного сложения с учётом сдвига
        summ = binSumm(summ, str( (int(binA) * m) * (10 ** i) ) )
        # Удаление последней цифры числа
        binB = binB[:-1]
    return int(summ, base = 2)

def columnMultiplicationPow(num1, num2):
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
            m = int( constNum1[ len(constNum1) - 1 ], base = 2 )
            # Выполнение двоичного сложения с учётом сдвига
            summ = binSumm(summ, str( (int(binA) * m) * (10 ** j) ) )
            # Удаление последней цифры числа
            constNum1 = constNum1[:-1]
        constNum1 = toBin(num1)
    return int(summ, base = 2)

print(columnMultiplication(2, 6))
print(columnMultiplicationPow(6, 3))


import math
import tkinter as tk

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

# Ваш код здесь:
def func(x, y):
    return x, y, 0

label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()