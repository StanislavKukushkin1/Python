import os
import numpy as np
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)
u = np.loadtxt(os.path.join(folder, 'numpy_initial_state.txt'))
states = [u.copy()]

for _ in range(255):
    u = u - 0.5 * (u - np.roll(u, 1))
    states.append(u.copy())

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].imshow(states, aspect='auto', origin='lower', extent=[0, len(u)-1, 0, 255])
axes[0].set_title('Изменение функции')
axes[0].set_xlabel('x')
axes[0].set_ylabel('Шаг времени')

axes[1].plot(u)
axes[1].set_title('После 255 шагов')
axes[1].set_xlabel('x')
axes[1].set_ylim(0, 10)
axes[1].grid()

plt.tight_layout()
plt.savefig(os.path.join(folder, 'episode3.png'))
plt.show()
