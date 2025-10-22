from _funcs import senterdifferanse

def f(x):
    return x**2 + 2*x + 1

def df(x):
    return 2*x + 2


x = 2
h = 0.1

print(
    (df(x) - senterdifferanse(f, x, h/4)) / (df(x) - senterdifferanse(f, x, h))
)

print(senterdifferanse(f, x, h))
print(senterdifferanse(f, x, h/4))

# ! hehhhh??
