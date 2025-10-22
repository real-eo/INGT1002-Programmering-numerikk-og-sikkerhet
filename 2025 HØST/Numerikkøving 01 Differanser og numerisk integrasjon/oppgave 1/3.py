from _funcs import senterdifferanse, log

def f(x): return log( 1+ x)

x = 0               # Verdi
h = 3/10            # Steglengde

print(senterdifferanse(f, x, h))