from pathlib import Path

import matplotlib.pyplot as plt

base = Path(__file__).resolve().parent
target = base / "results" / "episode3"
target.mkdir(parents=True, exist_ok=True)

students = []
with (base / "data" / "episode3" / "students.csv").open() as file:
    for line in file:
        teacher, group, mark = line.strip().split(";")
        students.append((teacher, group, int(mark)))

charts = (
    (0, [f"prep{i}" for i in range(1, 8)], "Оценки по преподавателям"),
    (1, [str(i) for i in range(751, 757)], "Оценки по группам"),
)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

for ax, (column, labels, title) in zip(axes, charts):
    bottom = [0] * len(labels)

    for mark in range(3, 11):
        counts = [
            sum(student[column] == name and student[2] == mark for student in students)
            for name in labels
        ]
        ax.bar(labels, counts, bottom=bottom, label=str(mark))
        bottom = [total + count for total, count in zip(bottom, counts)]

    ax.set_title(title)
    ax.set_ylabel("Количество студентов")
    ax.legend(title="Оценка", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
fig.savefig(target / "marks_distribution.png")
plt.close(fig)
