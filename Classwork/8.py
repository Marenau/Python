import math as m
import matplotlib.pyplot as matplotlib


def euclidean_distance(y, z):
    n = len(y)
    summ = 0
    for i in range(1, n + 1):
        summ += (y[i - 1] - z[i - 1]) ** 2
    return m.sqrt(summ)

def manhattan_distance(y, z):
    n = len(y)
    summ = 0
    for i in range(1, n + 1):
        summ += m.fabs(y[i - 1] - z[i - 1])
    return summ

def cosine_distance(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    a_norm = m.sqrt(sum(x ** 2 for x in a))
    b_norm = m.sqrt(sum(y ** 2 for y in b))
    return 1 - (dot_product / (a_norm * b_norm))

def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = matplotlib.subplots()
    # построение гистограммы с подписями
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])


distance_metrics = [euclidean_distance, manhattan_distance, cosine_distance]
visualize(distance_metrics, [1, 0.5, 1], [0.5, 2, 1], 1)
matplotlib.show()