import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

x = sp.symbols("x")
y = sp.Function("y")
solution = sp.dsolve(sp.Eq(sp.diff(y(x), x), -2 * y(x)), ics={y(0): sp.sqrt(2)})
print("Решение SymPy:", solution)

points = np.linspace(0, 10, 1000)
symbolic = sp.lambdify(x, solution.rhs, "numpy")(points)
numeric = solve_ivp(lambda t, z: -2 * z, (0, 10), [np.sqrt(2)],
                    t_eval=points, rtol=1e-10, atol=1e-12).y[0]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(points, symbolic, label="SymPy")
axes[0].plot(points, numeric, "--", label="SciPy")
axes[0].set_title("Решения")
axes[0].legend()

axes[1].plot(points, symbolic - numeric)
axes[1].set_title("Разность решений")

for ax in axes:
    ax.set_xlabel("x")
    ax.grid()

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "episode3.png"))
plt.show()
