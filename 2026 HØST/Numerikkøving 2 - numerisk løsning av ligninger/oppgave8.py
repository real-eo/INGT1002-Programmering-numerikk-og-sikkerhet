import numpy as np

def error(x):
    return abs(2*x - np.cos(x))   # avvik mhp. den opprinnelige ligningen

def fixedPoint(g, tol, strict):
    x = 0          # x_0 = 0
    n = 0
    # (a) "mindre enn eller lik" -> fortsett mens error > tol
    # (b) "lavere enn"           -> fortsett mens error >= tol
    while (error(x) > tol) if strict else (error(x) >= tol):
        x = g(x)
        n += 1
    return x, n

# (a)
ga = lambda x: np.cos(x)/2
xa, na = fixedPoint(ga, 1e-5, strict=True)

# (b)
def gb(x):
    return (2*x*(np.sin(x)+1) + np.cos(x)) / (4 + 2*np.sin(x))
xb, nb = fixedPoint(gb, 1e-3, strict=False)

print(na, xa)
print(nb, xb)