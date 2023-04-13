import matplotlib.pyplot as plt

# Функция для расчета последовательности значений
def logistic(r, x):
    return r * x * (1 - x)

# Задаем диапазон значений параметра бифуркации
mu_values = [mu / 1000 for mu in range(1000, 4000, 60)]

# Задаем количество итераций для каждого значения параметра бифуркации
num_iterations = 100

# Задаем количество последних итераций для построения диаграммы бифуркаций
num_last_iterations = 20

# Создаем список для хранения всех значений, полученных при итерациях
x_values = []
iter_values = []  # список для хранения номеров итераций

# Проходим по всем значениям параметра бифуркации
for mu in mu_values:
    # Задаем начальное значение для итераций
    x = 0.5
    # Проходим по всем итерациям
    for i in range(num_iterations):
        # Расчитываем следующее значение
        x = logistic(mu, x)
        # Если достигнуто нужное количество итераций, то добавляем значение в список
        if i >= (num_iterations - num_last_iterations):
            x_values.append([mu, x])
            iter_values.append(i)

# Строим диаграмму бифуркаций
plt.scatter(*zip(*x_values), c=iter_values, cmap='winter', s=20, linewidths=0)
plt.xlabel('mu')
plt.ylabel('x')
plt.show()
