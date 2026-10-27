
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)
data = os.path.join(folder, "data", "episode1")
result = os.path.join(folder, "results", "episode1")
os.makedirs(result, exist_ok=True)

for name in sorted(os.listdir(data)):
    if not name.endswith(".dat"):
        continue

    with open(os.path.join(data, name)) as file:
        n = int(file.readline())
        points = [list(map(float, file.readline().split())) for _ in range(n)]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, s=10)
    plt.gca().set_aspect("equal")
    plt.title(f"Количество точек: {n}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()

    filename = name.replace(".dat", ".png")
    plt.savefig(os.path.join(result, filename))
    plt.close()
