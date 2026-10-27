
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)
data = os.path.join(folder, "data", "episode2", "frames.dat")
result = os.path.join(folder, "results", "episode2")
os.makedirs(result, exist_ok=True)

with open(data) as file:
    rows = [list(map(float, line.split())) for line in file]

all_x = [x for row in rows[::2] for x in row]
all_y = [y for row in rows[1::2] for y in row]

for i in range(0, len(rows), 2):
    x = rows[i]
    y = rows[i + 1]
    number = i // 2

    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title(f"Кадр {number}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xticks(range(0, 17, 2))
    plt.yticks(range(-8, 13, 2))
    plt.xlim(min(all_x), max(all_x))
    plt.ylim(min(all_y) - 1, max(all_y) + 1)
    plt.grid()

    plt.savefig(os.path.join(result, f"frame_{number:03d}.png"))
    plt.close()
