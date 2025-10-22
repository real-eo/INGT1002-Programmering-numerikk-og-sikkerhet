from _funcs import trapesintegrasjon

def f(x):
    return (x**3 - 4*x)

print(trapesintegrasjon(f, a=-1, b=4, n=3))