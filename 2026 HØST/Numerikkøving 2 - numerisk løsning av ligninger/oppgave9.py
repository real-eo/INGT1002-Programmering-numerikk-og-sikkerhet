import numpy as np


# * Equation: 2*x = cos(x)

def error(x):
    return abs(2*x - np.cos(x))   # avvik mhp. den opprinnelige ligningen

def f(x):  return np.cos(x)/2 - x
def df(x): return -np.sin(x)/2 - 1

def newton(f, df, x0, tol):
    x = x0
    n = 0
    while error(x) > tol:         # "mindre enn eller lik" -> stop when error <= tol
        x = x - f(x)/df(x)        # Newton step
        n += 1
    return x, n

# (a)
xa, na = newton(f, df, 0, 1e-5)

# (b)
xb, nb = newton(f, df, 2, 1e-4)

print(na, xa)
print(nb, xb)