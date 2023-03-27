import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def generate_sprite(width, height):
    lst = [random.randint(0, 15) for s in range(2)]
    for i in range(0, len(lst) + 1, 2):
        lst.insert(i, 0)
    lst.insert(len(lst), 0)
    sprite = [[lst[random.randint(0, len(lst) - 1)] for i in range(width)] for j in range(height)]
    for i in range(height):
        sprite[i][:width//2] = sprite[i][width//2 + 1:][::-1]
    return sprite

sprite_width = 3
sprite_height = 5
big_sprite_height = 100
big_sprite_width = 200

big_sprite = np.zeros((big_sprite_height, big_sprite_width))

sprite_width = sprite_width if sprite_width % 2 != 0 else sprite_width + 1
for i in range(1, 50, 5):
    for j in range(1, 100, 5):
        big_sprite[i*2:i*2+sprite_height, j*2:j*2+sprite_width] = generate_sprite(sprite_width, sprite_height)

pico8_colors = ['#000000', '#1D2B53', '#7E2553', '#008751', '#AB5236', '#5F574F', 
                '#C2C3C7', '#FFF1E8', '#FF004D', '#FFA300', '#FFEC27', 
                '#00E436', '#29ADFF', '#83769C', '#FF77A8', '#FFCCAA']
cmap_pico8 = ListedColormap(pico8_colors)

plt.imshow(big_sprite, cmap=cmap_pico8)
plt.show()