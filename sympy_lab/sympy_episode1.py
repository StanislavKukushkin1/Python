import sympy as sp

lam, mu, rho = sp.symbols("lambda mu rho", positive=True)

A = sp.zeros(9)
A[0, 3] = -1 / rho
A[1, 4] = -1 / rho
A[2, 5] = -1 / rho
A[3, 0] = -(lam + 2 * mu)
A[4, 1] = -mu
A[5, 2] = -mu
A[6, 0] = -lam
A[8, 0] = -lam

for value, multiplicity in A.eigenvals().items():
    print("Собственное значение:", sp.simplify(value), "Кратность:", multiplicity)
