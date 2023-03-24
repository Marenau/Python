import random
import numpy as np
import matplotlib.pyplot as plt

def generate_sprite():
    sprite = [[random.randint(0, 1) for i in range(5)] for j in range(5)]
    for i in range(5):
        sprite[i][:2] = sprite[i][3:][::-1]
    return sprite

big_sprite = np.zeros((100, 200))

for i in range(1, 50, 5):
    for j in range(1, 100, 5):
        big_sprite[i*2:i*2+5, j*2:j*2+5] = generate_sprite()

plt.imshow(big_sprite, cmap='gray')
plt.show()

# import random
# import matplotlib.pyplot as plt

# def generate_sprite():
#     sprite = [[random.randint(0, 1) for i in range(5)] for j in range(5)]
#     for i in range(5):
#         sprite[i][:2] = sprite[i][3:][::-1]
#     return sprite

# big_sprite = [[0 for j in range(200)] for i in range(100)]

# for i in range(1, 50, 5):
#     for j in range(1, 100, 5):
#         sprite = generate_sprite()
#         for x in range(i*2, i*2+5):
#             for y in range(j*2, j*2+5):
#                 big_sprite[x][y] = sprite[x-i*2][y-j*2]

# plt.imshow(big_sprite, cmap='gray')
# plt.show()