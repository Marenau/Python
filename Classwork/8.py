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

def chebyshuov_distance(y, z):
    n = len(y)
    maximum = y[0]
    for i in range(1, n + 1):
        local_dist = abs(y[i - 1] - z[i - 1])
        if maximum < local_dist:
            maximum = local_dist
    return maximum

def square_euclidean_distance(y, z):
    sixth_ans = 0
    n = len(y)
    for i in range(0, n):
        sixth_ans += (y[i] - z[i]) ** 2
    return sixth_ans

def minkovskiy_distance(y, z):
    n = len(y)
    h = 5
    result = 0
    for i in range(0, n):
        result += m.fabs((y[i] - z[i]) ** h)
    return result ** (1 / h)

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


distance_metrics = [euclidean_distance, manhattan_distance, chebyshuov_distance, square_euclidean_distance, minkovskiy_distance]
visualize(distance_metrics, [1, 0.5, 1], [0.5, 2, 1], 1)
matplotlib.show()