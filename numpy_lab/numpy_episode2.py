import os
import numpy as np
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)
source = os.path.join(folder, 'signals')
result = os.path.join(folder, 'results', 'episode2')
os.makedirs(result, exist_ok=True)

for name in sorted(os.listdir(source)):
    if not name.endswith('.dat'):
        continue

    signal = np.loadtxt(os.path.join(source, name))
    smooth = np.array([
        signal[max(0, i - 9):i + 1].mean()
        for i in range(len(signal))
    ])

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True, sharey=True)
    axes[0].plot(signal)
    axes[0].set_title('Исходный сигнал')
    axes[1].plot(smooth)
    axes[1].set_title('После фильтра')

    for ax in axes:
        ax.set_xlabel('Номер измерения')
        ax.grid()

    plt.tight_layout()
    plt.savefig(os.path.join(result, os.path.splitext(name)[0] + '.png'))
    plt.close()
