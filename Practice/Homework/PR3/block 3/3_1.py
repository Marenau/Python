import random
import matplotlib.pyplot as plt

def generate_sprite():
    sprite = [[random.randint(0, 1) for i in range(5)] for j in range(5)]
    for i in range(5):
        sprite[i][:2] = sprite[i][3:][::-1]
    return sprite

sprite = generate_sprite()
plt.imshow(sprite, cmap='gray')
plt.show()