import os
import pandas as pd
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)
students = pd.read_excel(os.path.join(folder, "students_info.xlsx"))
results = pd.read_html(os.path.join(folder, "results_ejudge.html"))[0]

students["login"] = students["login"].astype("string")
results["User"] = results["User"].astype("string")

data = students.merge(results, left_on="login", right_on="User", how="inner")
faculty = data.groupby("group_faculty")["Solved"].mean().sort_index()
informatics = data.groupby("group_out")["Solved"].mean().sort_index()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
faculty.plot.bar(ax=axes[0], title="Факультетские группы")
informatics.plot.bar(ax=axes[1], title="Группы по информатике")
for ax in axes:
    ax.set_xlabel("Группа")
    ax.set_ylabel("Среднее количество решённых задач")
    ax.grid(axis="y")
plt.tight_layout()
plt.savefig(os.path.join(folder, "students.png"))
plt.show()

selected = data[(data["G"].fillna(0) > 10) | (data["H"].fillna(0) > 10)]

print("Студенты, прошедшие более одного теста в G или H:")
print(selected[["login", "group_faculty", "group_out"]].to_string(index=False))
print("\nКоличество по факультетским группам:")
print(selected["group_faculty"].value_counts().sort_index())
print("\nКоличество по группам информатики:")
print(selected["group_out"].value_counts().sort_index())
print("\nПроблемы в данных:")
print("Строки без логина:", students["login"].isna().sum())
print("Повторяющиеся логины:", students["login"].dropna().duplicated().sum())
print("Логины ejudge без соответствия в xlsx:",
      (~results["User"].isin(students["login"].dropna())).sum())
print("Логины xlsx без соответствия в ejudge:",
      (~students["login"].dropna().isin(results["User"])).sum())
