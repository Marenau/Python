import numpy as np
import matplotlib.pyplot as plt

def noise():
    arr = np.random.rand(200, 200)
    arr = (arr - 0.5) * 2
    return arr

noise_arr = noise()

fig, ax = plt.subplots(figsize=(18,6))
ax.plot(noise_arr.flatten())
plt.show()