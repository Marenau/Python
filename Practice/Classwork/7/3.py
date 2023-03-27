import matplotlib.pyplot as plt
import math

def noise():
    def noise(x, y):
        sc_x = x * 12.9898
        sc_y = y * 78.233
        return ( math.sin( sc_x + sc_y ) * 1000)
    arr = [noise(x, y) for x in range(50) for y in range(20)]
    return arr

noise_arr = noise()

fig, ax = plt.subplots(figsize=(18,6))
ax.plot(noise_arr)
plt.show()