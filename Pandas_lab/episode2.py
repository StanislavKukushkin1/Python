import os
import pandas as pd
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(folder, "flights.csv"))

result = data.groupby("CARGO").agg(
    flights=("CARGO", "size"),
    price=("PRICE", "sum"),
    weight=("WEIGHT", "sum")
)

print(result)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, column, title in zip(
    axes,
    ["flights", "price", "weight"],
    ["Количество рейсов", "Стоимость грузов", "Масса грузов"]
):
    ax.bar(result.index, result[column])
    ax.set_title(title)
    ax.grid(axis="y")

plt.tight_layout()
plt.savefig(os.path.join(folder, "flights.png"))
plt.show()
