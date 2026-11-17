import os
import numpy as np
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)

for filename in ("small_system.txt", "large_system.txt"):
    with open(os.path.join(folder, filename), encoding="utf-8") as file:
        n = int(file.readline())
        A = np.array([list(map(float, file.readline().split())) for _ in range(n)])
        b = np.array(list(map(float, file.readline().split())))

    x = np.linalg.solve(A, b)
    print(filename, "\nРешение:", x)
    print("Максимальная невязка:", np.max(np.abs(A @ x - b)))

    plt.figure(figsize=(12 if n > 10 else 6, 4))
    plt.bar(np.arange(n), x)
    plt.xlabel("Номер элемента")
    plt.ylabel("x[i]")
    plt.title(filename)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(os.path.join(folder, filename.replace(".txt", ".png")))

plt.show()
