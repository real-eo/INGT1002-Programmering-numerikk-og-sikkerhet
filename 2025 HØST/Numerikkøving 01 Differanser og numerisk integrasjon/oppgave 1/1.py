from _funcs import foroverdifferanse, sin


def f(x): return sin(x)

x = 0               # Verdi
h = 3/10            # Steglengde

print(foroverdifferanse(f, x, h))
