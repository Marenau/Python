import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def draw(figure_func, bbox=(-1.3,1.3)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    a = np.linspace(xmin, xmax, 80)
    b = np.linspace(ymin, ymax, 80)
    a1, a2 = np.meshgrid(a, b)
    for x in b:
        y, z = a1, a2
        X = figure_func(x, y, z)
        cest = ax.contour(X + x, y, z, [x], zdir='x', colors=('red'))
    for y in b:
        x, z = a1, a2
        X = figure_func(x, y, z)
        cest = ax.contour(x, X + y, z, [y], zdir='y', colors=('red'))
    for z in b:
        x, y = a1, a2
        X = figure_func(x, y, z)
        cest = ax.contour(x, y, X + z, [z], zdir='z', colors=('red'))
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
    ax.set_zlim3d(zmin, zmax)
    plt.show()

def figure_func(x, y, z):
    return (x**2 + 9*(y**2)/4 + z**2 - 1)**3 - x**2*z**3 - 9*(y**2)*(z**3)/200

draw(figure_func)