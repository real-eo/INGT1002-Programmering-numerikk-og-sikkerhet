from _funcs import bakoverdifferansen

# Beregen bakoverdifferansen av f ved x med steglengde h
def f(x): return x**3 - x + 1


x = -1              # Verdi
h = 3/10            # Steglengde

print(bakoverdifferansen(f, x, h))
