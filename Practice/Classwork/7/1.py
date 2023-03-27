import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 16 * (np.sin(t) ** 3)

def y(t):
    return 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

t = np.linspace(0, 2*np.pi)
x_t = x(t)
y_t = y(t)

plt.figure(figsize=(6,6))
plt.plot(x_t, y_t, color='red')
plt.show()

plt.figure(figsize=(6,6))
plt.plot(x_t, y_t, color='red')
plt.fill(x_t, y_t, color='red')
plt.show()
