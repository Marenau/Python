# import numpy as np
# import matplotlib.pyplot as plt


# class Chaos:
#     def __init__(self, mu, state):
#         self.mu = mu
#         self.state = state
    
#     def stabilize(self):
#         for _ in range(1000):
#             self.next()
    
#     def next(self):
#         pass

# class LogisticMap(Chaos):
#     def __init__(self, mu, state):
#         super().__init__(mu, state)
    
#     def next(self):
#         x = self.state
#         self.state = self.mu * x * (1 - x)
#         return self.state


# # Создаем объект LogisticMap
# o = LogisticMap(mu=4.0, state=0.1)

# # Стабилизируем систему
# o.stabilize()

# # Генерируем 1000 значений
# values = [o.next() for _ in range(100000)]

# # Строим гистограмму распределения
# hist, bins, _ = plt.hist(values, bins=20, density=True, alpha=0.5)
# plt.title('Распределение LogisticMap')
# plt.xlabel('Значение')
# plt.ylabel('Плотность вероятности')

# # Вычисляем коэффициенты аппроксимирующего многочлена
# coeffs = np.polyfit(bins[:-1], hist, 16)

# # Построение аппроксимирующей прямой
# x = np.linspace(0, 1, 1000)
# y = np.polyval(coeffs, x)
# plt.plot(x, y, 'b-')

# # Установка ограничений на ось y
# plt.ylim(0, 4)

# # Отображение графика
# plt.show()