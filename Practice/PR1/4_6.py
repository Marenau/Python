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

# Функция шума
def noise(x, y):
    sc_x = x * 12.9898
    sc_y = y * 78.233
    return (math.sin(sc_x + sc_y) * 43758.5453123) % 1

# Интерполирует значения шума в диапазоне от 0 до 1
def interpolate(f):
    return f * f * (3.0 - 2.0 * f)

# Ограничивает значение, чтобы оно лежало между двумя другими
def mix(x, y, a):
    return x * (1 - a) + y * a

# Алгоритм value noise
def val_noise(x, y):
    x *= 5
    y *= 5
    x_int = int(x)
    y_int = int(y)
    x_frac = x - x_int
    y_frac = y - y_int

    a = noise(x_int, y_int)
    b = noise(x_int + 1, y_int)
    c = noise(x_int, y_int + 1)
    d = noise(x_int + 1, y_int + 1)

    u1 = interpolate(x_frac)
    u2 = interpolate(y_frac)

    return mix(a, b, u1) + (c - a) * u2 * (1 - u1) + (d - b) * u1 * u2


# Ваш код здесь:
def func(x, y):
    # Переменная частоты
    value = 0
    # Пременная амплитуды
    amplitude = 0.6
    # Пременная для увеличения частоты на каждом уровне
    frequency = 1.0
    
    # Алгоритм фрактального шума (генерация шума на каждом уровне)
    for i in range(0, 10):
        value += amplitude * val_noise(x * frequency, y * frequency)
        frequency *= 2
        amplitude *= 0.5
    
    return value, value, 1


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()