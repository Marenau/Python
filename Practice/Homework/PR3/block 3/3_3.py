import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def generate_sprite():
    sprite = [[random.randint(0, 255) for i in range(5)] for j in range(5)]
    for i in range(5):
        sprite[i][:2] = sprite[i][3:][::-1]
    return sprite

big_sprite = np.zeros((100, 200))

for i in range(1, 50, 5):
    for j in range(1, 100, 5):
        big_sprite[i*2:i*2+5, j*2:j*2+5] = generate_sprite()

pico8_colors = ['#000000', '#1D2B53', '#000000', '#7E2553', '#008751', '#000000', '#AB5236', '#000000', '#5F574F', 
                '#000000', '#C2C3C7', '#000000', '#FFF1E8', '#FF004D', '#000000', '#FFA300', '#000000', '#FFEC27', 
                '#000000', '#00E436', '#000000', '#29ADFF', '#83769C', '#000000', '#FF77A8', '#000000', '#FFCCAA']
cmap_pico8 = ListedColormap(pico8_colors)

plt.imshow(big_sprite, cmap=cmap_pico8)
plt.show()